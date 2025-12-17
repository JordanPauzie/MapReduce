# Step 1 Mapper

import sys
import re
import string
from nltk.corpus import stopwords

STOP_WORDS = set(stopwords.words('english'))

in_content = False
marker_count = 0

for line in sys.stdin:
    line = line.rstrip()
    
    # Track marker lines to distinguish header from content
    if '======================================================================' in line:
        marker_count += 1
        # First marker: start of header (ignore, don't process)
        # Second marker: end of header, start of content
        if marker_count % 2 == 0:
            in_content = True
        else:
            # Odd markers (1st, 3rd, 5th, etc.): end of content, start of next header
            in_content = False
        continue

    # Process content only (between second and third markers)
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