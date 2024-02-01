# Import necessary packages
import math

# Define constants
G = 9.81  # Gravity. Units: m/s^2
K = 0.01  # Air resistance factor

# Define variables
t = 7.0  # Time. Units: seconds

# Calculate y_N(t)
y_N = (0.5) * G * (t ** 2)

# Calculate y_air(t)
y_air = (1 / K) * math.log(math.cosh(t * math.sqrt(G * K)))

# Calculate the difference: E(t)
y_diff = math.fabs(y_N - y_air)

# Print the results
print("t = %.1fs, y_N(t) = %.2em, y_air(t) = %.2em, y_diff = %.4em"%(t, y_N, y_air, y_diff))

# My code's output was as follows:
# t = 7.0s, y_N(t) = 2.40e+02m, y_air(t) = 1.51e+02m, y_diff = 8.9175e+01m
