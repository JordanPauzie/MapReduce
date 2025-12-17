import sys

# Step 2 Reducer
# Keep one (word, year)'s count in memory at a time (streaming approach)
current_word = None
current_year = None
current_count = 0

# For current word, collect year counts (only one word's data at a time)
current_word_years = []  # List of (year, count) for current word

def generate_bar_chart(year_counts, max_count):
    """Generate ASCII bar chart for a word's year distribution"""
    if max_count == 0:
        return ""
    
    chart_lines = []
    # Scale bar length (max 50 characters)
    scale = 50.0 / max_count if max_count > 0 else 1
    
    for year, count in sorted(year_counts):
        bar_length = int(count * scale)
        bar = '#' * bar_length
        chart_lines.append(f"  {year}: {count:4d} |{bar}")
    
    return '\n'.join(chart_lines)

def output_word_analysis(word, year_counts):
    """Output analysis for a complete word"""
    if not year_counts:
        return
    total = sum(count for _, count in year_counts)
    max_count = max(count for _, count in year_counts) if year_counts else 0
    
    print(f"Word: {word} (Total: {total})")
    print(generate_bar_chart(year_counts, max_count))
    print()

for line in sys.stdin:
    line = line.strip()
    if not line:
        continue
    
    word, year, count = line.split('\t')
    count = int(count)

    # If this is the same (word, year) combination, accumulate the count
    if current_word == word and current_year == year:
        current_count += count
    else:
        # New (word, year) encountered
        if current_word is not None and current_year is not None:
            # Save the previous (word, year) count
            current_word_years.append((current_year, current_count))
        
        # Check if we're moving to a new word
        if current_word is not None and current_word != word:
            # Output the previous word's complete analysis
            output_word_analysis(current_word, current_word_years)
            # Clear for new word
            current_word_years = []
        
        # Start tracking new (word, year)
        current_word = word
        current_year = year
        current_count = count

# Don't forget the last (word, year)
if current_word is not None and current_year is not None:
    current_word_years.append((current_year, current_count))

# Output the last word's analysis
if current_word is not None:
    output_word_analysis(current_word, current_word_years)