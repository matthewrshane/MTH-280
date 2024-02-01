# Define variables
triangle_num = 0
squares = 0

# Loop over n: [0, 20]
for n in range(1, 21):
    # Calculate the current triangle number
    triangle_num += n

    # Calculate the current square number
    squares += (n ** 2)

    # Calculate the difference of (T_n)^2 - S_n
    diff = (triangle_num ** 2) - squares

    # Print the difference
    print(diff)