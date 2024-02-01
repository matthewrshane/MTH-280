import numpy as np
import matplotlib.pyplot as plt

# Define constants
a = 0.2065               # morbidity rate
b = 0.1                  # recovery rate (I -> R) (1 / 10 days)
K2 = 19.23 * (10**(-3))  # rate of exhaustion (S_res -> S_exh)
K3 = 0.01                # constant of transition to a state of ignorance (S_exh -> S_ign)
q = 85.2 * (10**3)       # stress response rate (S_ign + 2I -> S_res + 2I)
I_0 = 19.2 * (10**(-6))  # initial fraction of infected people (I[0])
P = 3.0 * (10**8)        # total population
NUMBER_OF_DAYS = 150     # number of days to simulate

def SIRss_model():
    """ Uses the SIRss model to plot the number of susceptible, infected, and recovered people in the US"""
    
    # Define locally used variables
    S_ign = np.zeros(NUMBER_OF_DAYS)     # susceptible but ignorant or uninformed
    S_res = np.zeros(NUMBER_OF_DAYS)     # susceptible and reasonably resistant
    S_exh = np.zeros(NUMBER_OF_DAYS)     # susceptible but exhausted
    I = np.zeros(NUMBER_OF_DAYS)         # currently infected
    R = np.zeros(NUMBER_OF_DAYS)         # recovered cases
    CC = np.zeros(NUMBER_OF_DAYS)        # the cumulative total of cases (I + R)

    # Set the initial values
    I[0] = I_0
    R[0] = 0
    S_ign[0] = 1 - I_0
    S_res[0] = 0
    S_exh[0] = 0
    CC[0] = I[0] + R[0]

    # Loop through each day
    for t in range(1, NUMBER_OF_DAYS):
        # Calculate each of the variables
        S_ign[t] = S_ign[t - 1] + ((-q * S_ign[t - 1] * (I[t - 1]**2)) - (a * S_ign[t - 1] * I[t - 1]) + (K3 * S_exh[t - 1]))
        S_res[t] = S_res[t - 1] + ((q * S_ign[t - 1] * (I[t - 1]**2)) - (K2 * S_res[t - 1]))
        S_exh[t] = S_exh[t - 1] + ((-a * S_exh[t - 1] * I[t - 1]) + (K2 * S_res[t - 1]) - (K3 * S_exh[t - 1]))
        I[t] = I[t - 1] + ((a * S_exh[t - 1] * I[t - 1]) + (a * S_ign[t - 1] * I[t - 1]) - (b * I[t - 1]))
        R[t] = R[t - 1] + ((b * I[t - 1]))
        CC[t] = I[t] + R[t]

    # Split the plot into subplots
    fig, ax1 = plt.subplots(layout="constrained")

    # Configure and plot the susceptible data
    color = 'k'
    ax1.set_xlabel('Number of days')
    ax1.set_ylabel('Normalized cases for S', color=color)
    ax1.plot(range(NUMBER_OF_DAYS), S_ign, "-k", label="Susceptible ignorant")
    ax1.plot(range(NUMBER_OF_DAYS), S_res, "--k", label="Susceptible resistant")
    ax1.plot(range(NUMBER_OF_DAYS), S_exh, ":k", label="Susceptible exhausted")
    ax1.tick_params(axis='y', labelcolor=color)

    # Configure and plot the infected/recovered data
    ax2 = ax1.twinx()
    color = 'tab:blue'
    ax2.set_ylabel('Normalized cases for I, R, and CC', color=color)
    ax2.plot(range(NUMBER_OF_DAYS), I, "-b", label="Infected people")
    ax2.plot(range(NUMBER_OF_DAYS), R, "--b", label="Recovered people")
    ax2.plot(range(NUMBER_OF_DAYS), CC, "-r", label="Cumulative cases")
    ax2.tick_params(axis='y', labelcolor=color)

    # Configure the plot
    plt.title("SIRss model of Covid-19 (Normalized % of population vs # of days)")
    plt.figlegend(loc=9, bbox_to_anchor=(0.5, 0.95))
    plt.xlim([0, NUMBER_OF_DAYS])

    # Show the plot
    plt.show()

    # Import and graph COVID cases data from the day 100 cases were reported to that day plus NUMBER_OF_DAYS
    cases_per_day = np.loadtxt("owid-covid-data.csv", delimiter=",", usecols=(5), skiprows=283375, max_rows=NUMBER_OF_DAYS)
    plt.bar(range(NUMBER_OF_DAYS), cases_per_day, width=0.4)

    # Use numpy to calculate the derivative of CC (multiplied by the population as CC is normalized)
    # The derivative of the cumulative total of cases is roughly the amount of new cases per day, as
    # visualized by the figure from the BBC
    CC_prime = np.gradient(CC, 1.0) * P
    plt.plot(range(NUMBER_OF_DAYS), CC_prime, "-k", label="CC'")

    # Configure the second plot
    plt.xlabel("Number of days")
    plt.ylabel("Daily new cases")
    plt.title("SIRss model of number of cases per day")
    plt.legend(loc=2)
    plt.xlim([0, NUMBER_OF_DAYS])

    # Show the second plot
    plt.show()

    # ----- STUFF BELOW IS NOT IN HW5 -----
    # Calculate the value of R^2
    # Calculate the actual CC by summing cases_per_day
    CC_actual = np.zeros(len(cases_per_day))
    sum = 0
    for i in range(len(cases_per_day)):
        sum += cases_per_day[i]
        CC_actual[i] = sum

    # Plot CC_actual and CC
    plt.plot(range(NUMBER_OF_DAYS), CC_actual, ":r", label="TCC")
    plt.plot(range(NUMBER_OF_DAYS), CC * P, "-r", label="CC")

    # Configure the second plot
    plt.xlabel("Number of days")
    plt.ylabel("Total confirmed cases")
    plt.title("SIRss model of number of cases per day")
    plt.legend(loc=2)
    plt.xlim([0, NUMBER_OF_DAYS])

    plt.show()

    # Calculating the value of R^2
    SSR = 0.0
    for i in range(len(CC_actual)):
        SSR += (CC_actual[i] - CC[i])**2

    avg = np.average(CC_actual)
    SST = 0.0
    for i in range(len(CC_actual)):
        SST += (CC_actual[i] - avg)**2

    R_squared = 1.0 - (SSR / SST)
    print("R^2 = %.5f"%R_squared)


    # ----- END ADDITIONS -----


# Call the function
SIRss_model()