# Problem 3:
#   The prime factors of 13195 are 5, 7, 13, and 29.

#   What is the largest prime factor of the number 600851475143?
from analyser import primeFinder


# Store the given number and half of the given as an integer
# This makes it easy to adjust for different scenarios
given = 600851475143
half = int(given / 2) + 1

# Initialise a number to store the greatest prime factor
greatestPrime = None

# Start a loop to check all possible factors, start from the greatest
# Range avoids the factors 1 and the number itself
for i in range(2, half):
    if (given % i) == 0:
        greaterFactor = int(given / i)
        if(primeFinder(greaterFactor)):
            greatestPrime = greaterFactor
            break

# Check to make sure the loop found a solution
# Output the result to the user
if greatestPrime != None:
    print(f"The greatest prime factor of the given number {given} is: ")
    print(greatestPrime)
else:
    print(f"The given number {given} is prime.")