#https://adventofcode.com/2022/day/3
#Groups strings into groups of three and find common letter.
#Lowercase item types a through z have priorities 1 through 26.
#Uppercase item types A through Z have priorities 27 through 52.

import pandas as pd

# Load the Excel sheet into a DataFrame
df = pd.read_excel('AdventOfCode3.xlsx', header=None)

# Define a function that computes the sum of the common letters in three rows
def compute_common(row1, row2, row3):
    common = set(row1) & set(row2) & set(row3)
    common_sum = sum([ord(c) - 96 if c.islower() else ord(c) - 38 for c in common])
    return common_sum

total_sum = 0

# Process the data in groups of three rows
for i in range(0, len(df), 3):
    row1, row2, row3 = df.iloc[i:i+3, 0]
    common_sum = compute_common(row1, row2, row3)
    print(f"Group {i//3+1}: Common sum = {common_sum}")
    total_sum += common_sum

# Print the total sum
print(f"The total sum of common letters is {total_sum}")
