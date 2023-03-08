#https://adventofcode.com/2022/day/2
#Rock,paper,scissors; each Rock (X), paper (Y), scissor (Z) that I play results in a score of 1, 2, 3, respectively
#for the opponent: Rock (A), paper (B), scissor (C)
#Winning scores 6, draw scores 3, loosing scores 0.
#calculate the total score of 2500 games that are arranged in a vertical dataframe

import pandas as pd

# Load the Excel file into a pandas DataFrame
df = pd.read_excel('AdventOfCode2.xlsx', header=None)

# Make a copy of the dataframe before modifying it
df_copy = df.copy()

# Convert the values to strings and extract the third character
df[0] = df[0].str[2]

# Calculate the sum based on the third character
sum_x = df.loc[df[0] == 'X'].shape[0]
sum_y = 2 * df.loc[df[0] == 'Y'].shape[0]
sum_z = 3 * df.loc[df[0] == 'Z'].shape[0]
total_sum_singlePlayer = sum_x + sum_y + sum_z

# Print the results
print(f"Total sum for X: {sum_x}")
print(f"Total sum for Y: {sum_y}")
print(f"Total sum for Z: {sum_z}")
print(f"Total sum: {total_sum_singlePlayer}")

# Initialize the sum variable
total_sum = 0

# Iterate over each row in the copied DataFrame
for row in df_copy.itertuples(index=False):
    code = row[0]  # Get the code from the first column of the current row
    if code == 'A X' or code == 'B Y' or code == 'C Z':
        total_sum += 3
    elif code == 'A Y' or code == 'B Z' or code == 'C X':
        total_sum += 6
    else:
        total_sum += 0

# Print the total sum
print(f"Total sum: {total_sum}")

final_sum=total_sum+total_sum_singlePlayer
print(final_sum)
