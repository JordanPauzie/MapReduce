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

in_content = False
in_header = False
current_year = None

for line in sys.stdin:
    original_line = line
    line = line.rstrip()
    
    # Track marker lines
    if '======================================================================' in line:
        if not in_header and not in_content:
            # First marker: entering header section
            in_header = True
            current_year = None
        elif in_header:
            # Second marker: leaving header, entering content
            in_header = False
            in_content = True
        elif in_content:
            # Third marker: leaving content, entering next header
            in_content = False
            in_header = True
            current_year = None
        continue

    # Extract year from header section
    if in_header and line.startswith('Year:'):
        year_match = re.search(r'Year:\s*(\d{4})', original_line)
        if year_match:
            current_year = year_match.group(1)

    # Process content only
    if in_content and current_year is not None:
        # Extract words - use \w which includes Unicode word characters
        # This matches the same logic as step1_mapper for consistency
        words = re.findall(r'\b\w+\b', original_line.lower())
        
        for word in words:
            # Clean word: remove any non-alphabetic characters (handles Unicode punctuation)
            clean = re.sub(r'[^a-z]', '', word)
            
            # Filter: minimum length 3, alphabetic only, in top 25 words
            if len(clean) >= 3 and clean.isalpha() and clean in TOP_WORDS:
                output = f"{clean}\t{current_year}\t1"
                print(output)