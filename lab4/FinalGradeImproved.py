# This program will compute a final MTH-280 grade
# Author: Matthew Shane
# Date: 02/02/2023

# Define grades in the following variables (Final grade B+)
hw = [ 90.0, 97.0, 83.0 ]
lab = [ 100.0, 100.0, 90.0, 90.0, 80.0 ]
exam1 = 77.0
exam2 = 91.0

# Calculate the average hw and lab grades
hw = sum(hw) / len(hw)
lab = sum(lab) / len(lab)

# Calculate the grade with weighted averages
grade = (0.40 * hw) + (0.15 * lab) + (0.20 * exam1) + (0.25 * exam2)

# Print the results
print("Final grade: %.0f (%.2f)" % (round(grade), grade))

# Round the grade for letter purposes
grade = round(grade)

# Default the letter grade to failing
letter_grade = "failing"

# Check for the letter grade
if (grade >= 93): letter_grade = "A"
elif (grade >= 90): letter_grade = "A-"
elif (grade >= 87): letter_grade = "B+"
elif (grade >= 83): letter_grade = "B"
elif (grade >= 60): letter_grade = "less than a B"

# Print the letter grade
print("My grade is %s." % letter_grade)
