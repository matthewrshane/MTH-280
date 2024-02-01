import numpy as np
import math
import matplotlib.pyplot as plt

def exp_approx(x, N):
    """ Approximates the function e^x using the following summation:
        sum{n=0 -> N-1}[(x^n)/n!]
        -----
        x -- the variable x used to approximate e^x

        N -- the number of loops used to approximate e^x"""
    
    # Define locally used variables
    exp_sum = np.zeros(N)    # stores the values of exp[i]
    error_abs = np.zeros(N)  # stores the absolute error values
    error_rel = np.zeros(N)  # stores the relative error values
    factorial = 1.0          # stores the value of (n - 1)! to calculate n!

    # Define the constant true value of e^x
    TRUE_VALUE = np.exp(x)

    # Loop from n = 0 to n = N - 1
    for n in range(0, N):
        # Calculate the value of n! (n! = 1 at n=0)
        factorial = (factorial * n) if n > 0 else 1.0

        # Calculate the value of the next term
        try:
            next_term = ((x**n)/factorial)
        except OverflowError as oe:
            # Handle the overflow error
            next_term = 0

        # Set the value of exp_sum[n] while not calling exp_sum[-1]
        exp_sum[n] = exp_sum[n - 1] + next_term if n > 0 else next_term

        # Calculate and set the absolute error
        error_abs[n] = math.fabs(TRUE_VALUE - exp_sum[n])

        # Calculate and set the relative error
        error_rel[n] = error_abs[n] / TRUE_VALUE

    # Calculate the minimum absolute and relative errors
    min_err_abs = np.amin(error_abs)
    index_min_err_abs = np.argmin(error_abs)
    min_err_rel = np.amin(error_rel)
    index_min_err_rel = np.argmin(error_rel)

    # Print these values to the console along with the values of (x, N)
    print("[(x, N) = (%d, %d)] The minimum absolute error = %.2e at index i = %d."%(x, N, min_err_abs, index_min_err_abs))
    print("[(x, N) = (%d, %d)] The minimum relative error = %.2e at index i = %d."%(x, N, min_err_rel, index_min_err_rel))

    # Plot the absolute and relative errors using a semilogy figure
    plt.semilogy(range(0, N), error_abs, "-k", label="Absolute error")
    plt.semilogy(range(0, N), error_rel, "-r", label="Relative error")
    
    # Configure the plot
    plt.suptitle("Absolute and relative error for approximation of e^x")
    plt.title("x = %d, N = %d"%(x, N))
    plt.ylabel("Absolute/relative error")
    plt.xlabel("Number of terms")
    plt.legend(loc=1)

    # Show the plot
    plt.show()

# Call the function for each set of (x, N)
exp_approx(1, 20)
exp_approx(20, 100)
exp_approx(100, 200) # causes OverflowError
exp_approx(-5, 50)
exp_approx(-10, 60)
exp_approx(-20, 100)


# Answers for part C below
# Do the errors saturate?
#   Yes, the values of the error can only be reduced to around 10^(-16),
#   as this is the underlying machine epsilon for a 64 bit floating point
#   number in python. Thus, this is the smallest possible error for a
#   floating point number in python.
#
# Is the absolute error ever misleadingly large or small?
#   Yes, as in different test cases the absolute error is much smaller or
#   much larger than the relative error, which is more accurate as a form of
#   error detection.
#
# Do overflow or underflow errors become problematic?
#   Yes, as in the (100, 200) case the program will throw an error and not
#   produce a plot to show.
#
# Is the series evaluated at x = 20 or x = -20 a better numerical
# approximation to the exponential function?
#   The series evaluated at x = -20 is a better numerical approximation
#   to the exponential function as the minimum error is lower.