# Step 1 Mapping:
/Users/jordanpauzie/miniforge3/bin/python \
/Users/jordanpauzie/Documents/GitHub/MapReduce/step1_mapper.py \
< /Users/jordanpauzie/Documents/GitHub/MapReduce/cleaned_text.txt \
> step1_mapped.txt

# Step 1 Reducing:
/Users/jordanpauzie/miniforge3/bin/python \
/Users/jordanpauzie/Documents/GitHub/MapReduce/step1_reducer.py \
< /Users/jordanpauzie/Documents/GitHub/MapReduce/step1_mapped.txt \
> step1_reduced.txt

# Step 2 Mapping:
/Users/jordanpauzie/miniforge3/bin/python \
/Users/jordanpauzie/Documents/GitHub/MapReduce/step2_mapper.py \
< /Users/jordanpauzie/Documents/GitHub/MapReduce/cleaned_text.txt \
> step2_mapped.txt

# Step 2 Reducer:
/Users/jordanpauzie/miniforge3/bin/python \
/Users/jordanpauzie/Documents/GitHub/MapReduce/step2_reducer.py \
< /Users/jordanpauzie/Documents/GitHub/MapReduce/step2_mapped.txt \
> step2_analysis.txt