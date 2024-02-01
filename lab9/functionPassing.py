import numpy as np

# Define constants
SAMPLE_POINTS = 10000

def find_max(y, a, b):
    """INPUT
       =====
       y: the function y(x) to maximize. This function must accept
          as input a numpy array and output a numpy array.
          
       a: the interval's left boundary
       b: the interval's right boundary
       
       OUTPUT
       =====
       max of y(x) such that x is in the interval [a, b]"""
    
    # Generate many x-values in [a, b]
    x_vals = np.linspace(a, b, SAMPLE_POINTS)

    # Calculate corresponding y-values
    y_vals = y(x_vals)

    # Find and return the max of these points
    return np.max(y_vals)

# Define several y(x) functions

def y1(x):
    return 0.5 * x

def y2(x):
    return np.sin(x)

# Call the function on y1(x) and y2(x)
print(find_max(y1, -1.0, 1.0))
print(find_max(y2, -1.0, 2.0))