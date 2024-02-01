# This program will compute a final MTH-280 grade
# Author: Matthew Shane
# Date: 02/02/2023

# Define grades in the following variables
hw = 90
lab = 100
exam1 = 77
exam2 = 91

# Calculate the grade with weighted averages
grade = (0.40 * hw) + (0.15 * lab) + (0.20 * exam1) + (0.25 * exam2)

# Print the results
print("Final grade: %.2f" % grade)
