# Step 1 Mapper

import sys
import re
import string
from nltk.corpus import stopwords

STOP_WORDS = set(stopwords.words('english'))

in_header = True
in_content = False

for line in sys.stdin:
    line = line.rstrip()
    
    # Detect marker lines (======================================================================)
    if '======================================================================' in line:
        if in_header:
            # Second marker: end of header, start of content
            in_header = False
            in_content = True
        elif in_content:
            # Third marker: end of content
            in_content = False
            in_header = True  # Ready for next book
        continue

    # Process content only
    if in_content:
        # Extract words from lines
        words = re.findall(r'\b[\w\']+\b', line)

        for word in words:
            # Clean word: remove punctuation, lowercase
            clean = re.sub(r'[^\w\s]', '', word)
            clean = clean.lower()
            
            # Filter: minimum length 3, alphabetic only, not a stop word
            if len(clean) >= 3 and clean.isalpha() and clean not in STOP_WORDS:
                    output = f"{clean}\t1"
                    print(output)