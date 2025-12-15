# Step 1 Mapper

import sys
import re
import string
from nltk.corpus import stopwords

STOP_WORDS = set(stopwords.words('english'))

in_content = False
toc = False
chapter = False

for line in sys.stdin:
    line = line.rstrip()
    
    # Check for start of content marker
    if '*** START OF' in line:
        in_content = True
        continue
        
    # Check for end of content marker
    if '*** END OF' in line:
        in_content = False
        break

    # Check for Table of Contents
    if line == 'Contents':
        toc = True
        continue

    if toc and line != '':
        chapter = True
        continue

    if toc and chapter and line == '':
        toc = False
        chapter = False
        continue

    if (not in_content) or toc:
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