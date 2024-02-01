import matplotlib.pyplot as plt
import numpy as np

# Define constants
N = 50

# Create a list of integers in the range [0, N)
i = np.arange(0, N)

# Compute the points of the circle
x_vals = 0.5 * np.cos(2 * np.pi * i / N)
y_vals = 0.5 * np.sin(2 * np.pi * i / N)

# Visually test these values by plotting them on a graph
plt.plot(x_vals, y_vals, "bo")
plt.title("Set of points approximating a circle of r = 1/2, N = 50")
plt.show()

# Create a perimeter value to total up each distance
perimeter = 0

# Loop through each point to calculate the distance to the next
for index in i:
    perimeter += np.sqrt((x_vals[0 if index == N - 1 else index + 1] - x_vals[index])**2 +
                         (y_vals[0 if index == N - 1 else index + 1] - y_vals[index])**2)

# Print the approximate value of pi
print("N: %d, pi: %.8f"%(N, perimeter))

# Values from running the program for N = [50, 500, 5000, 50000]
# N: 50, pi: 3.13952598
# N: 500, pi: 3.14157198
# N: 5000, pi: 3.14159245
# N: 50000, pi: 3.14159265

# Since a circle can be defined as the set of all points that are
# equidistant from the center of the circle, it shares its set
# of points with an N sided polygon as N -> infinity.
# Therefore, as N converges to infinity, the set of points will
# converge to a perfect circle whose perimeter (circumference)
# is equal to pi.