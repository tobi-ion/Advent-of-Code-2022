#https://adventofcode.com/2022/day/1
#find the highest three sums in a list with vertically arranged numbers; after each blank cell, a new sum starts

import openpyxl

# Load the Excel sheet
workbook = openpyxl.load_workbook('AdventOfCode1.xlsx')
worksheet = workbook.active

# Iterate over the cells and compute the sum between blank spaces
sums = []
sum_1 = 0
for row in worksheet.iter_rows():
    for cell in row:
        if cell.value is not None:
            try:
                num = float(cell.value)
                sum_1 += num
            except ValueError:
                pass
        else:
            sums.append(sum_1)
            sum_1 = 0

# Append the last sum to the list
sums.append(sum_1)

# Get the three highest sums
highest_sums = sorted(sums, reverse=True)[:3]

print("The three highest sums are:", highest_sums)
sum_of_three_highest_sums = sum(highest_sums)
print("The sum of the three highest sums is:",sum_of_three_highest_sums)
