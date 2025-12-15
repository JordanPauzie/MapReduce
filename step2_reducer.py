# Step 1 Reducer
word_counts = {}

for line in sys.stdin:
    line = line.strip()

    # Parse input: word\tcount
    # Aggregate counts
    if word in word_counts:
    else:

# Sort by count (descending) and output

# Print result
for word, count in sorted_words:
    print(f"{word}\t{count}")