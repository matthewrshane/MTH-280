# This program will compute wind-chill
# Author: Matthew Shane
# Date: 02/16/2023

# Define a value of T
T = 10

# Get the range of wind speeds
wind_speeds = range(0, 65, 5)

# Loop through every wind speed
for V in wind_speeds:
    Twc = 35.74 + (0.6215 * T) - (35.75 * (V**0.16)) + (0.4275 * T * (V**0.16))
    print("T = %2.0f, wind = %2.0f, wind chill = %2.0f" % (T, V, round(Twc)))
