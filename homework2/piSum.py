import math

# Declare constants
N = 20
SQRT_12 = math.sqrt(12)
NEGATIVE_ONE_THIRD = -1.0/3.0

# Declare variables
S_N = 0

# Loop through the range [0, N]
for k in range(N + 1):
    # Increment S_N by the value according to the current k
    S_N += (SQRT_12 * math.pow(NEGATIVE_ONE_THIRD, k)) / (2.0 * k + 1)

    # Calculate E_N
    E_N = math.fabs(S_N - math.pi) / math.pi

    # Print the results
    print('k = {:.0f} | S_N = {:0.8f} | E_N = {:0.2E}'.format(k, S_N, E_N))

    # The smallest value of N that approximates pi to 5 digits successfully (3.14159) is 8,
    # providing the answer S_N = 3.14159977, with an error rate of E_N = 2.27E-06.