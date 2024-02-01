import math as m
import numpy as np
import time

# Tests the computation of sin(x) using python lists
def time_list(N):
    t = time.time()

    xs = range(N)
    y = []
    for x in xs:
        y.append(m.sin(x))

    elapsed = time.time() - t
    print("list computation: elapsed time %f, for %i points"%(elapsed,N))


# Tests the computation of sin(x) using numpy arrays
def time_numpy(N):
    t = time.time()
    xs = np.arange(N)
    y = np.sin(xs)
    elapsed = time.time() - t
    print("numpy computation: elapsed time %f, for %i points"%(elapsed,N))

time_list(1000000)      # list computation: elapsed time 0.096635, for 1000000 points
time_numpy(1000000)     # numpy computation: elapsed time 0.007012, for 1000000 points
time_list(10000000)     # list computation: elapsed time 0.968807, for 10000000 points
time_numpy(10000000)    # numpy computation: elapsed time 0.073882, for 10000000 points
time_list(100000000)    # list computation: elapsed time 10.687146, for 100000000 points
time_numpy(100000000)   # numpy computation: elapsed time 1.231837, for 100000000 points

# Using numpy arrays to compute the sin(x) is much faster than using python lists, as shown by the fact that
# when computing 100,000,000 data points, the numpy method takes only around 1 second to compute, whereas
# the python list counterpart takes over 10 seconds to compute the data.
