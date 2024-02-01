# euler.py will numerically check Euler's equation
# Author: Matthew Shane
# Date: 02/09/2023

import cmath as cm

# Initialize theta with an angle of 0 rad
theta = 0.0

# Continue looping until theta is equal to 6.0
while theta <= 6.0:
    # Calculate the left-hand side of Eq.1: e^(i*theta)
    LHS = cm.exp(theta * 1.0j)

    # Calculate the right-hand side of Eq.1 cos(theta) + i*sin(theta)
    RHS = cm.cos(theta) + 1.0j * cm.sin(theta)

    # Calculate the absolute difference between the LHS and RHS
    difference = abs(LHS - RHS)

    # Print the results
    print("Left side  = ", LHS)
    print("Right side = ", RHS)
    print("theta = %.1f, |LHS - RHS| of eulers equation = %.1e"%(theta, difference))
    
    # Increment the value of theta by 0.5 rad
    theta += 0.5
