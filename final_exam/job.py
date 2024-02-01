

def job_earnings(hourlyRate, hoursPerWeek, costGasPerGal, galPerMile, distance):
    ''' Calculates your total earnings per week taking into account travel cost.

        -----
        Input:\n
        hourlyRate - the rate ($/hr) at which you are paid\n
        hoursPerWeek - the amount of hours you work per week (days per week * hours per day)\n
        costGasPerGal - the cost of gas per gallon\n
        galPerMile - the number of gallons of gas your car uses per mile of travel (1 / mpg)\n
        distance - the one-way distance in miles to your job

        -----
        Output:\n
        the amount, in dollars, you make per week after accounting for travel costs'''
    
    # Calculate the earnings without travel costs
    earningsWithoutTravel = (1 - 0.2) * hourlyRate * hoursPerWeek

    # Calculate the cost of travel
    costOfTravel = (2 * 5) * costGasPerGal * galPerMile * distance

    # Return the overall earnings for the week
    return earningsWithoutTravel - costOfTravel

# Test case for task 1: rate = 20, hours = 10, cost/gal = 4, gal/mi = (1/15), distance = 30
print("Test case for task 1: Earnings = $%.2f"%job_earnings(20, 10, 4, 1/15, 30))

# Loop through each possibility of 1-8 hours per day
for hoursPerDay in range(1, 9):
    # Calculate hours per week
    hoursPerWeek = hoursPerDay * 5

    # Calculate and print the earnings for both job 1 and job 2 using their respective rates and distances
    print("working %d hour%s per day (%d hour%s per week). Job 1 earnings = %.2f"%
          (hoursPerDay, "s" if hoursPerDay > 1 else "", hoursPerWeek, "s" if hoursPerWeek > 1 else "", job_earnings(17, hoursPerWeek, 4, 1/25, 5)))
    print("working %d hour%s per day (%d hour%s per week). Job 2 earnings = %.2f"%
          (hoursPerDay, "s" if hoursPerDay > 1 else "", hoursPerWeek, "s" if hoursPerWeek > 1 else "", job_earnings(19, hoursPerWeek, 4, 1/25, 23)))
    
    # At 20 hours per week, Job 2's earnings become more favorable than Job 1's earnings.