#https://adventofcode.com/2022/day/5
#grid of letters where a series of operations moves x letters from column y to the top of column z (reversing the order of the letters x or not)


import pandas as pd

# Load the input data from the Excel file
data = pd.read_excel('AdventOfCode5.xlsx', header=None, names=['instructions'])



import pandas as pd

# Load the input data from the Excel file
data = pd.read_excel('AdventOfCode5.xlsx', header=None, names=['instructions'])

# Initialize the grid of letters
input_data = [
    ['', '', '', 'G', 'W', '', '', 'Q', ''],
    ['Z', '', '', 'Q', 'M', '', 'J', 'F', ''],
    ['V', '', '', 'V', 'S', 'F', 'N', 'R', ''],
    ['T', '', '', 'F', 'C', 'H', 'F', 'W', 'P'],
    ['B', 'L', '', 'L', 'J', 'C', 'V', 'D', 'V'],
    ['J', 'V', 'F', 'N', 'T', 'T', 'C', 'Z', 'W'],
    ['G', 'R', 'Q', 'H', 'Q', 'W', 'Z', 'G', 'B'],
    ['R', 'J', 'S', 'Z', 'R', 'S', 'D', 'L', 'J']
]

# Get the number of columns in the input data
num_cols = len(input_data[0])

# Initialize list of concatenated strings
strings = []

# Iterate over each column
for col_idx in range(num_cols):
    # Initialize a string for this column
    col_string = ''
    # Iterate over each row in this column
    for row_idx in range(len(input_data)):
        # Append the character to the column string
        col_string += input_data[row_idx][col_idx]
    # Append the concatenated column string to the list
    strings.append(col_string)

# Print the concatenated strings
print(strings)

for instruction in data['instructions']:
    # Split the instruction into its components
    parts = instruction.split()
    x = int(parts[1])
    y = int(parts[3]) - 1 # adjust index for 0-based indexing
    z = int(parts[5]) - 1 # adjust index for 0-based indexing
    # Get the first x letters of string y and remove them from y
    letters = strings[y][:x]
    strings[y] = strings[y][x:]
    # Add the letters in reverse order to the beginning of string z (Advent of Code 5.1)
    #strings[z] = letters[::-1] + strings[z]

    # Add the letters in original order to the beginning of string z (Advent of Code 5.2)
    strings[z] = letters[::] + strings[z]
    # Print the intermediate list of strings
    #print(strings)


# Print the final list of strings
print(strings)

# Get the first letter of each string
first_letters = ''.join([s[0] for s in strings])

# Print the first letter of each string
print(first_letters)







