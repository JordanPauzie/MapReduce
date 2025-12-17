# Step 2 Mapper

import sys
import re

TOP_WORDS = set()

# Load top 25 words from step 1 output
with open("step1_reduced.txt") as f:
    for i in range(25):
        line = f.readline()
        if not line:
            break
        word, _ = line.strip().split('\t')
        TOP_WORDS.add(word)

# State tracking
in_header = False
in_content = False
current_year = None

for line in sys.stdin:
    original_line = line
    line = line.rstrip()
    
    # Detect marker lines (======================================================================)
    if '======================================================================' in line:
        if not in_header and not in_content:
            # First marker: start of header section
            in_header = True
            current_year = None
        elif in_header:
            # Second marker: end of header, start of content
            in_header = False
            in_content = True
        elif in_content:
            # Third marker: end of content
            in_content = False
            current_year = None
        continue

    # Extract year from header section
    if in_header and line.startswith('Year:'):
        # Extract year from "Year: 1887" format
        year_match = re.search(r'Year:\s*(\d{4})', original_line)
        if year_match:
            current_year = year_match.group(1)

    # Process content only
    if in_content and current_year is not None:
        # Extract words from lines
        words = re.findall(r'\b[\w\']+\b', original_line)

        for word in words:
            # Clean word: remove punctuation, lowercase
            clean = re.sub(r'[^\w\s]', '', word)
            clean = clean.lower()
            
            # Filter: minimum length 3, alphabetic only, in top 25 words
            if len(clean) >= 3 and clean.isalpha() and clean in TOP_WORDS:
                output = f"{clean}\t{current_year}\t1"
                print(output)