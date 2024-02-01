import math

# Declare constants
MAGIC_VALUE = (1 + math.sqrt(2)) ** 4

# Declare variables
square_triangle_numbers = [1, 36]
triangle_number = 36
k = 9

# Loop through triangle numbers
while len(square_triangle_numbers) < 11:
    # Find the next triangle number
    triangle_number += k
    k += 1

    # Check if this triangle number is a perfect square
    root = math.sqrt(triangle_number)
    if int(root + 0.5) ** 2 == triangle_number:
        # Add this triangle number to the list of square triangle numbers
        square_triangle_numbers.append(triangle_number)

# Print the list of square triangle numbers
print(square_triangle_numbers)

# Loop through the square triangle numbers
for i in range(len(square_triangle_numbers) - 1):
    ratio = square_triangle_numbers[i + 1] / square_triangle_numbers[i]
    print('i = {:.0f}: N_i+1/N_i = {:.4f} | Diff = {:.4E}'
          .format(i, ratio, math.fabs(ratio - MAGIC_VALUE)))
    
# Print the 'Magic Value' determined earlier
print('(1 + sqrt(2))^4 = {:.4f}'.format(MAGIC_VALUE))