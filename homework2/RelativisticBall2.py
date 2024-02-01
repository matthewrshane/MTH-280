import math

# Declare constants
START_HEIGHT = 829.8
GRAVITY = 9.81
SPEED_OF_LIGHT = 299792458.0

# Declare variables
time = 0.0
height = START_HEIGHT

# Loop until the break condition is reached
while True:
    # Calculate using EQ 1 (Newton)
    y_newton = (0.5) * GRAVITY * math.pow(time, 2)

    # Calculate using EQ 2 (Einstein)
    y_einstein = (2.0) * (math.pow(SPEED_OF_LIGHT, 2) / GRAVITY) * math.pow(math.sinh((0.5) * (GRAVITY / SPEED_OF_LIGHT) * time), 2)

    # Calculate the difference between the two methods
    y_diff = math.fabs(y_newton - y_einstein)

    # Update the height variable
    height = START_HEIGHT - y_newton

    # Break if the height is <= 0
    if height <= 0: break

    # Print the results
    print('Time: {:.2f}s | yN(t) = {:.2E}m | yE(t) = {:.2E}m | E(t) = {:.2E}m'.format(time, y_newton, y_einstein, y_diff))

    # The maximum discrepancy between yN(t) and yE(t) occurs at time = 13.00s and is calculated as 1.26E-11m.
    # This is on a scale of picometers, which is close to the distance between atomic nuclei in a white dwarf star,
    # according to Wikipedia [https://en.wikipedia.org/wiki/List_of_examples_of_lengths].
    # You would likely be unable to perform this experiment in a real world setting due to the very tiny discrepancy
    # between the equations.

    # Update the time variable
    time += 0.25
