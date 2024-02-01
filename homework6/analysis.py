import numpy as np
import matplotlib.pyplot as plt
import scipy.integrate
import math

# Define constants
a = -1
b = 1

def my_function(x):
    """ function to integrate"""
    return ((np.sin(102 * x))**2)/(1 + (x**2))


def riemann_sum(rectangles, xleft=0.0, xright=2.0):
    """ Input
        =====
        rectangles --- number of rectangles used to compute the Riemann sum
        xleft  -- left value of integration (default = 0.0)
        xright -- right value of integration (default = 2.0)"""
    
    # Compute the width of each rectangle
    dx = (xright - xleft) / rectangles

    # Generate a uniform grid (equally spaced) of x-values
    # Each x-value is located in the middle of a rectangle
    x0 = xleft + dx/2.0
    xend = xright - dx/2.0
    x_points = np.linspace(x0, xend, rectangles)

    # Evaluate the function at the middle of each rectangle
    y_values = my_function(x_points)

    # Print x and y values -- code check
    # print(y_values)
    # print(x_points)

    # Numerically compute the integral by a Riemann sum
    integral = np.sum(y_values) * dx

    return integral

# Calculate the true value of the integral.
I_true = scipy.integrate.quad(my_function, a, b)[0]

# Create arrays
N_vals = np.zeros(8)
I_vals = np.zeros(8)
E_vals = np.zeros(8)

# Loop through values 0-7 (for N = 10^0 to 10^7)
for i in range(0, 8):
    # Compute the value of N
    N_vals[i] = 10 ** i

    # Compute the value of I
    I_vals[i] = riemann_sum(rectangles=int(N_vals[i]), xleft=a, xright=b)

    # Compute the value of E
    E_vals[i] = math.fabs(I_true - I_vals[i])

    # Print these values
    print("N = %8d | I = %.10f | I_N = %.10f | E_N = %.9e"%(N_vals[i], I_true, I_vals[i], E_vals[i]))

# Produce a graph of AN^(-2)
N = 1.0
E_model = N * (N_vals ** (-2))

# Plot the E_N on the y-axis and the N values on the x-axis
plt.loglog(N_vals, E_vals, "-k", label="Error values")
plt.loglog(N_vals, E_model, "--r", label="Error model (AN^-2)")

# Configure the plot
plt.title("Error of integral vs # of rectangles")
plt.ylabel("Error of integral")
plt.xlabel("Number of rectangles")
plt.legend(loc=1)

# Show the plot
plt.show()

# As shown in the plot, as the number of rectangles increases (-> on the x-axis)
# the error value decreases. Additionally, the graph of AN^-2 is plotted in red,
# which shows how the riemann sum model follows this expected model.