import numpy as np
import matplotlib.pyplot as plt

# Load in the dataset
dataset = np.loadtxt("gravityWave.dat") 

# Separate the values of t and h(t)
t, h_t = dataset.T

# Calculate the index of the max value of h(t)
max_h_t_index = np.argmax(h_t)

# Get the max value of t and h(t)
max_t = t[max_h_t_index]
max_h_t = h_t[max_h_t_index]

# Plot the values of t vs. h(t)
plt.plot(t, h_t, "-b", label="Gravitational Wave")
plt.plot([max_t], [max_h_t], "r*", label="Max Value")

# Configure the plot
plt.title("Gravitational Wave Signal")
plt.xlabel("Time (seconds)")
plt.ylabel("Signal")

# Show the plot
plt.show()
