# Step 2 Mapper

import sys
import re
import string
from nltk.corpus import stopwords

STOP_WORDS = set(stopwords.words('english'))

for line in sys.stdin:
    line = line.rstrip()

    # Check for start of content marker
    if '*** START OF' in line:

    # Check for end of content marker
    if '*** END OF' in line:

    # Check for Table of Content

    # Process content only
    if in_content:
        # Extract words from lines
        words = re.findall(r'\b[\w\']+\b', line)

        for word in words:
        # Clean word: remove punctuation, lowercase
        # Filter: minimum length 3, alphabetic only, not a stop word
        if len(word) >= 3 and word.isalpha() and word not in STOP_WORDS: