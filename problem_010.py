# Problem 10:
#   The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

#   Find the sum of all the primes below two million.

import math
from analyser import primeFinder

def sieve_of_eratosthenes(limit):
    # Initialise a list that stores all numbers under limit as a Boolean
    num_list = [True for i in range(limit)]
    num_list[0] = False
    num_list[1] = False

    for current in range(2, math.floor(math.sqrt(limit)) + 1):
        if primeFinder(num_list[current]):
            for multiple in range(pow(current, 2), limit, current):
                num_list[multiple] = False

    return [prime for prime in range(limit) if num_list[prime] is True]


# Create a variable that can be edited to the user's needs
limit = 2_000_000

prime_list = sieve_of_eratosthenes(limit)

# Print the output to the user.
print(f"The sum of all primes under {limit} is:")
print(sum(prime_list))