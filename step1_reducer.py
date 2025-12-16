import sys

# Step 1 Reducer
word_counts = {}

for line in sys.stdin:
    line = line.strip()

    word, count = line.split('\t')

    # Aggregate counts
    if word in word_counts:
        word_counts[word] += int(count)
    else:
        word_counts[word] = int(count)

# Sort by count (descending) and output
sorted_words = sorted(word_counts.items(), key=lambda x: x[1], reverse=True)

# Print result
for word, count in sorted_words:
    print(f"{word}\t{count}")