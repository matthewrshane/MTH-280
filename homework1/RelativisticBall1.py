import math

# Declare constants
TIME = 7.0
GRAVITY = 9.81
SPEED_OF_LIGHT = 299792458.0

# Calculate using EQ 1 (Newton)
y_newton = (0.5) * GRAVITY * math.pow(TIME, 2)

# Calculate using EQ 2 (Einstein)
y_einstein = (2.0) * (math.pow(SPEED_OF_LIGHT, 2) / GRAVITY) * math.pow(math.sinh((0.5) * (GRAVITY / SPEED_OF_LIGHT) * TIME), 2)

# Calculate the difference between the two methods
y_diff = math.fabs(y_newton - y_einstein)

# Print the results
print('y_newton   = {:.2E}m'.format(y_newton))   # 2.40E+02 meters
print('y_einstein = {:.2E}m'.format(y_einstein)) # 2.40E+02 meters
print('y_diff     = {:.4E}m'.format(y_diff))     # 1.1369E-12 meters
