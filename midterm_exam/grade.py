# Define constants
lab_avg = 87.0
hw_avg = 89.0
midterm = 90.0

# Loop over every possible final exam score [0, 100]
for final_exam in range(0, 101):
    # Calculate the final grade using the following percentages:
    # Homework Projects: 40%
    # Computing Labs: 15%
    # Midterm Exam: 20%
    # Final Exam: 25%
    final_grade = (0.40 * hw_avg) + (0.15 * lab_avg) + (0.20 * midterm) + (0.25 * final_exam)

    # Print the results of this final exam grade.
    print("Final exam grade = %3d, My final grade is %.2f"%(final_exam, final_grade))
    