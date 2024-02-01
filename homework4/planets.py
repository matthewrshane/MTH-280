import numpy as np
import matplotlib.pyplot as plt

# Declare constants
NUMBER_OF_CALCULATIONS = 500
GRAVITY = 6.7 * (10**(-11))   # Newton's constant in m^3/(kg s^2)
MASS_OF_SUN = 2.0 * (10**30)  # Mass of sun in kg
GM = GRAVITY * MASS_OF_SUN    # Precomputed value of G * M
KM_TO_M = 1000                # Constant to convert km to m
M_TO_KM = 1/1000              # Constant to convert m to km
MPS_TO_KPH = 3.6              # Constant to convert m/s to km/hr

# Load in the planetary data
data = np.loadtxt('planetdata.txt')
dist = data[:,0]  # km
vel = data[:,1]   # km/hr

# Get the min and max radial distances
min_dist = np.amin(dist) * KM_TO_M  # Convert to meters
max_dist = np.amax(dist) * KM_TO_M  # Convert to meters

# Calculate the distance between values that we will use for calculation
delta_dist = (max_dist - min_dist) / NUMBER_OF_CALCULATIONS

# Create the list of r values to use in computation
r_vals = np.arange(min_dist, max_dist, delta_dist)

# Compute values of v(r) = sqrt(G*M/r) for every radius
v_vals = np.sqrt(GM / r_vals) * MPS_TO_KPH  # Convert m/s to km/hr

# Convert r_vals into km
r_vals *= M_TO_KM

# Plot the computed equation
plt.plot(r_vals, v_vals, 'ko--', linewidth=2, markersize=0, label="Predicted values")

# Plot the data points
plt.plot(dist, vel, "ro", label="Actual values")

# Configure the graph
plt.xlabel("Distance to sun (km)")
plt.ylabel("Orbital velocity (km/hr)")
plt.title("Distance to sun vs Orbital velocity")
plt.legend()

# Show the plot
plt.show()
