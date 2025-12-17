import sys

# Step 1 Reducer
word_year_counts = {}

for line in sys.stdin:
    line = line.strip()

    word, year, _ = line.split('\t')

    # Aggregate counts
    if word not in word_year_counts:
        word_year_counts[word] = {}

    if year not in word_year_counts[word]:
        word_year_counts[word][year] = 0

    word_year_counts[word][year] += 1

# Print year analysis
for word in word_year_counts:
    print(f"Word: {word} (Total: {sum(word_year_counts[word].values())})")
    for year in sorted(word_year_counts[word]):
        count = word_year_counts[word][year]
        print(f"{year}: {count}")
    print("\n")