# Problem 3:
#   The prime factors of 13195 are 5, 7, 13, and 29.

#   What is the largest prime factor of the number 600851475143?


def primeFinder(number):
    """ A basic function for determining whether an integer is 
    a prime, returning True for prime values and False otherwise """
    # First, make sure the factor is NOT an even number or 2
    if (number % 2 == 0) and (number != 2):
        return False

    half = int(number / 2) + 1
    # Loop that checks each odd number that can possibly be a factor
    # If the number divides by i, the number is NOT prime
    for i in range(3, half, 2):
        if (number % i) == 0:
            return False

    # If all previous checks fail, then the number has no factors
    # Therefore, it is prime
    return True

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