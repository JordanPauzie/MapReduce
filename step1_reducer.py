import sys

# Step 1 Reducer
# Keep one word's count in memory at a time (streaming approach)
current_word = None
current_count = 0

# Collect all word-count pairs for sorting
word_counts = []

for line in sys.stdin:
    line = line.strip()
    if not line:
        continue
    
    word, count = line.split('\t')
    count = int(count)

    # If this is the same word, accumulate the count
    if current_word == word:
        current_count += count
    else:
        # New word encountered - output previous word if exists
        if current_word is not None:
            word_counts.append((current_word, current_count))
        
        # Start tracking new word
        current_word = word
        current_count = count

# Don't forget the last word
if current_word is not None:
    word_counts.append((current_word, current_count))

# Sort by count (descending) and output
sorted_words = sorted(word_counts, key=lambda x: x[1], reverse=True)

# Print result
for word, count in sorted_words:
    print(f"{word}\t{count}")