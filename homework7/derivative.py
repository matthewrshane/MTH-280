import matplotlib.pyplot as plt
import numpy as np

def finite_difference(y, a, dx):
    """ Computes the approximate derivative of y at a using the following formula:
        y'(a) = [y(a + dx) - y(a)]/dx where dx -> 0 (dx =/= 0)
        
        Input
        =====
        y  -- the function y(x) to differentiate
        a  -- the value a where the derivative is evaluated
        dx -- the difference in x-values to use when computing the derivative (as x -> 0, the derivative becomes more accurate)
              
        Output
        ======
        The value of the finite difference approximation for the derivative
        of y(x) at x = a"""
    
    return (y(a + dx) - y(a)) / dx

# Define the function sin(x) to differentiate
def y(x):
    return np.sin(x)

# Define a set of dx values and colors to use for the plots
dx_vals = [4, 2, 1, 0.5, 0.1]
colors = ["b+", "y+", "g+", "r+", "m+"]

# Loop through each value of dx to be plotted
for i in range(len(dx_vals)):
    # Calculate the x-values and values of dy/dx at each x-value
    x_vals = np.linspace(-np.pi, np.pi, 1000)
    dy_dx = finite_difference(y, x_vals, dx_vals[i])

    # Plot the graph of these dy/dx values
    plt.plot(x_vals, dy_dx, colors[i], label="dx = %.2f"%dx_vals[i])

# Calculate the mathematically exact value (cos(x)) and plot on the graph
x_vals = np.linspace(-np.pi, np.pi, 1000)
y_vals = np.cos(x_vals)
plt.plot(x_vals, y_vals, "-k", label="cos(x)")

# Configure the plot
plt.title("Finite difference approximation of d/dx sin(x)")
plt.legend(loc=1)

# Show the plot
plt.show()
