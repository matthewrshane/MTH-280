import math

def users(year):
    ''' Approximates the number of Facebook users for a given year.
        =====
        Input
        year: the year to estimate (full 4-digit year e.g. 2006)'''
    e_factor = math.exp((year - 2009.975) / 0.85)
    return (1.4 * (10**9) * e_factor) / (1 + e_factor)

# Prints the year and predicted amount of users for 2006-2050
for y in range(2006, 2051):
    print("year = %4d, Facebook users = %.6e"%(y, users(y)))