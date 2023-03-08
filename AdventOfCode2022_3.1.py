#https://adventofcode.com/2022/day/3
#divide string in two parts, find common letter (case-sensitive) in the two parts and assign values:
#Lowercase item types a through z have priorities 1 through 26.
#Uppercase item types A through Z have priorities 27 through 52.

import pandas as pd

# Load the Excel sheet into a DataFrame
df = pd.read_excel('AdventOfCode3.xlsx', usecols=[0], header= None, names=None)

# Define a function that divides a string into two halves
def divide_string(s):
    midpoint = len(s) // 2
    return s[:midpoint], s[midpoint:]

# Define a function that computes the sum of the common letters in two halves of a string
def compute_common(half1, half2):
    common = set(half1) & set(half2)
    common_sum = sum([ord(c) - 96 if c.islower() else ord(c) - 38 for c in common])
    compute_common.total_sum += common_sum
    return common_sum

compute_common.total_sum = 0 # initialize the total sum to zero

# Divide each string into two halves and compute the sum of common letters
for index, row in df.iterrows():
    half1, half2 = divide_string(row[0])
    common_sum = compute_common(half1, half2)
    #print(f"Row {index + 1}: Common sum = {common_sum}")

# Print the total sum
print(f"The total sum of common letters is {compute_common.total_sum}")
