import matplotlib.pyplot as plt
from math import sin

# Define constants
X_RANGE = [-5, 15]
Y_RANGE = [-1.5, 1.5]
DX = 0.05

# Define lists of x and y values
xVals = []
yVals = []

# Loop over integers from [0, 300]
for i in range (0, 301):
    # Calculate the actual value of x and store it
    x = i * DX
    xVals.append(x)

    # Calculate the value of y=sin(x) and store it
    yVals.append(sin(x))

# Plot values using matplotlib
plt.plot(xVals, yVals, "ro")

# Configure the plot
plt.xlim(X_RANGE)
plt.ylim(Y_RANGE)
plt.xlabel("x values")
plt.ylabel("y values")
plt.title("Figure made by Matthew Shane")
plt.legend(["sine(x)"], loc=1)

# Save the plot
plt.savefig("mySimplePlot.png", bbox_inches="tight")