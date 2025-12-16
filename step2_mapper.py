# Step 2 Mapper

import sys
import re
import string
from nltk.corpus import stopwords

KNOWN_DATES = {
    # Arthur Conan Doyle - Sherlock Holmes
    'a study in scarlet': 1887,
    'the sign of the four': 1890,
    'the adventures of sherlock holmes': 1892,
    'the memoirs of sherlock holmes': 1894,
    'the hound of the baskervilles': 1902,
    'the return of sherlock holmes': 1905,
    'the valley of fear': 1915,
    'his last bow': 1917,
    'the adventures of the bruce-partington plans': 1908,
    # Edgar Allan Poe
    'the works of edgar allan poe': 1845,
    # Agatha Christie
    'the mysterious affair at styles': 1920,
    'the murder on the links': 1923,
    'poirot investigates': 1924,
    'the secret adversary': 1922,
    'the man in the brown suit': 1924,
    # G. K. Chesterton - Father Brown
    'the innocence of father brown': 1911,
    'the wisdom of father brown': 1914,
    # Wilkie Collins
    'the moonstone': 1868,
    # Gaston Leroux
    'the mystery of the yellow room': 1907,
    'the secret of the night': 1914,
    # A. A. Milne
    'the red house mystery': 1922,
    # Dorothy L. Sayers
    'whose body': 1923,
    # Arthur J. Rees
    'the hand in the dark': 1920,
}

TOP_WORDS = set()

with open("step1_reduced.txt") as f:
    for i in range(25):
        line = f.readline()
        word, _ = line.strip().split('\t')
        TOP_WORDS.add(word)

in_content = False
toc = False
chapter = False
curr_title = ""
curr_release_date = 0

for line in sys.stdin:
    line = line.rstrip()        
    
    # Check for start of content marker
    if '======================================================================' in line:
        in_content = True
        continue
        
    # Check for end of content marker
    if '======================================================================' in line:
        in_content = False
        continue

    # If title found
    line = re.sub(r'[^\w\s]', '', line)
    line = line.lower()
    if line in KNOWN_DATES:
        curr_title = line
        curr_release_date = KNOWN_DATES[line]

    # Process content only
    if in_content:
        # Extract words from lines
        words = re.findall(r'\b[\w\']+\b', line)

        for word in words:
            # Clean word: remove punctuation, lowercase
            clean = re.sub(r'[^\w\s]', '', word)
            clean = clean.lower()
            
            # Filter: minimum length 3, alphabetic only, not a stop word
            if len(clean) >= 3 and clean.isalpha() and clean in TOP_WORDS:
                    output = f"{clean}\t{curr_release_date}\t1"
                    print(output)