import numpy as np
from matplotlib import pyplot as plt
import math

# Define constants
gamma = 20 * 24                             # Typical recovery time in hours (20 days)
R_0 = [1.7, 4, 10]                          # Number of newly infected people per infected person (3 different scenarios)
P = 3.0 * (10**8)                           # Total approximate population of the US
NUMBER_OF_DAYS = np.array([360, 180, 120])  # Total number of days to calculate and plot data for
TOTAL_HOURS = NUMBER_OF_DAYS * 24           # Total number of hours, based on the # of days


# Define a function that creates a plot of S, I, and R vs number of days for a given value of R_0
# using the SIR model
def SIR_model(index):
    # Ensure the index is between [0, 2]
    if index < 0 or index > len(R_0) - 1: index = 0

    # Set the value of r_0 for this index
    r_0 = R_0[index]

    # Define the variables used to track the disease spread
    I = np.zeros(TOTAL_HOURS[index])  # Number of infected people, initially 10^5
    I[0] = 1.0 * (10**5)
    R = np.zeros(TOTAL_HOURS[index])  # Number of recovered people, initially 0
    R[0] = 0
    S = np.zeros(TOTAL_HOURS[index])  # Number of susceptible people, calculated by P - I[0]
    S[0] = P - I[0]

    # Precompute local constants
    r_gammaP = (r_0 / (gamma * P))  # Computes R_0/(gamma * P) (eq. 2)
    gamma_inverse = (1.0 / gamma)   # Computes 1/gamma (eq. 3)

    # Loop through each hour up to the max number of days
    for t in range(TOTAL_HOURS[index] - 1):
        # Calculate and append to the arrays of S, I, and R using Eqs. 2, 3, and 4
        S[t + 1] = S[t] - (r_gammaP * I[t] * S[t])                           # Eq. 2
        I[t + 1] = I[t] + (r_gammaP * I[t] * S[t]) - (gamma_inverse * I[t])  # Eq. 3
        R[t + 1] = R[t] + (gamma_inverse * I[t])                             # Eq. 4

        # Ensure the total of (S + I + R) is within 0.1% of P
        if math.fabs((S[t + 1] + I[t + 1] + R[t + 1]) - P) > (P * 0.001):
            print("S + I + R is not within 1%% of P! t: %d, S: %e, I: %e, R: %e, P: %e"
                  %(t + 1, S[t + 1], I[t + 1], R[t + 1], P))


    # Create a plot for the data
    plt.plot(range(NUMBER_OF_DAYS[index]), S[::24], "--r", label="Susceptible people")
    plt.plot(range(NUMBER_OF_DAYS[index]), I[::24], "--g", label="Infected people")
    plt.plot(range(NUMBER_OF_DAYS[index]), R[::24], "--b", label="Recovered people")

    # Configure the plot
    plt.xlabel("Number of days")
    plt.ylabel("Number of people")
    plt.suptitle("SIR model of Covid-19 (# of people vs. # of days)")
    plt.title("R_0 = %.1f"%r_0)
    plt.legend(loc=1)
    plt.xlim([0, NUMBER_OF_DAYS[index]])
    plt.ylim([0, P])

    # Calculate the max value and index of infected people
    max_infected = np.max(I)
    max_index = np.argmax(I)
    
    # Compute this max index as the day and hour of the day
    max_day = math.floor(max_index / 24)
    max_hour = (max_index % 24)

    # Print the max to the console
    print("The max # of infected people for R_0 = %.1f is %e, occuring on day %d, at hour %d (hour = %d)"
          %(r_0, max_infected, max_day, max_hour, max_index))
    
    # Max values for each R_0:
    # R_0 = 1.7:  2.995927e+07
    # R_0 = 4.0:  1.211769e+08
    # R_0 = 10.0: 2.012888e+08
    
    # Annotate the plot with this max value
    plt.annotate("Max Infected", (NUMBER_OF_DAYS[index] * 0.02, max_infected + (P * 0.02)))
    plt.hlines(y=max_infected, xmin=0, xmax=max_day)
    plt.vlines(x=max_day, ymin=0, ymax=max_infected)

    # Show the plot
    plt.show()

    

# Call the SIR model function for R_0[0-2]
# Uncommenting the other function calls will produce a graph corresponding
# with that value of R_0[index]
SIR_model(0)
#SIR_model(1)
#SIR_model(2)