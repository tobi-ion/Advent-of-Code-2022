#https://adventofcode.com/2022/day/2
#Anyway, the second column says how the round needs to end: X means you need to lose, Y means you need to end the round in a draw, and Z means you need to win. Good luck!"
#The total score is still calculated in the same way, but now you need to figure out what shape to choose so the round ends as indicated

import pandas as pd

# Load the Excel file into a pandas DataFrame
df = pd.read_excel('AdventOfCode2.xlsx', header=None)

# Make a copy of the dataframe before modifying it
df_copy = df.copy()

# Initialize the sum variable
total_sum = 0

# Iterate over each row in the DataFrame
for row in df.itertuples(index=False):
    for code in row[0].split():
        if code == 'X':
            total_sum += 0
        elif code == 'Y':
            total_sum += 3
        elif code == 'Z':
            total_sum += 6

# Print the total sum
print(f"Total sum: {total_sum}")


# Initialize the sums variables

# Make a copy of the dataframe before modifying it
df_copy = df.copy()

# Initialize the sums variables
sum_1 = 0

# Iterate over each row in the DataFrame
for row in df_copy.itertuples(index=False):
    code = row[0]  # Get the code from the first column of the current row
    if code == 'A X' or code == 'B Z' or code == 'C Y':
        sum_1 += 3
    elif code == 'A Z' or code == 'B Y' or code == 'C X':
        sum_1 += 2
    elif code == 'A Y' or code == 'C Z' or code == 'B X':
        sum_1 += 1

# Print the sums
print(f"Sum 1: {sum_1}")

final_sum= total_sum + sum_1
print(final_sum)