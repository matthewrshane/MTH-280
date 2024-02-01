import numpy as np
import matplotlib.pyplot as plt

def riemann_sum(integrand, xleft, xright, rectangles):
    """ Input
        =====
        integrand  -- function to integrate
        xleft      -- left value of integration
        xright     -- right value of integration
        rectangles -- number of rectangles used to compute the Riemann sum"""
    
    # Compute the width of each rectangle
    dx = (xright - xleft) / rectangles

    # Generate a uniform grid (equally spaced) of x-values
    # Each x-value is located in the middle of a rectangle
    x0 = xleft + dx/2.0
    xend = xright - dx/2.0
    x_points = np.linspace(x0, xend, rectangles)

    # Evaluate the function at the middle of each rectangle
    y_values = integrand(x_points)

    # Print x and y values -- code check
    # print(y_values)
    # print(x_points)

    # Numerically compute the integral by a Riemann sum
    integral = np.sum(y_values) * dx
    print("integral = %1.15e"%integral)
    #print("integral error = %1.15e"%(integral - 1.0))