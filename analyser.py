"""A collection of modules for calculating primes, palindromes,
and more related to the Euler Problems."""

import math

def primeFinder(number):
    """ A basic function for determining whether an integer is 
    a prime, returning True for prime values and False otherwise """
    # First, make sure the factor is NOT an even number or 2
    if (number % 2 == 0) and (number != 2):
        return False

    limit = int(math.sqrt(number)) + 1

    # If the number divides by i, the number is NOT prime
    for i in range(3, limit, 2):
        if (number % i) == 0:
            return False

    # If all previous checks fail, then the number has no factors
    # Therefore, it is prime
    return True

def numPalindromeFinder(number):
    """ 
    A function designed to find palindromes of specifically 
    integer values, returning True if the number is a palindrome 
    and False otherwise. 
    """
    numString = str(number)
    length = len(numString)

    # Numbers with only one digit are palindromes
    if length == 1:
        return True

    # From here, split the number in half
    left = numString[:length//2]
    # Check to see if the length is even or odd
    # If odd, remove the number directly in the middle
    if length % 2 == 0:
        right = numString[(length//2):]
    else: 
        right = numString[(length//2) + 1:]

    # Check to see if the left side is equal to the reverse of
    # the right
    if left == (right[::-1]):
        return True
    else:
        return False

def numDivisorFinder(number):
    """A function designed to find all divisors in a given integer,
    returning a list of all values found."""
    # Keeps track of how many divisors are found
    divisors = 0

    limit = int(math.sqrt(number)) + 1

    for i in range(1, limit):
        if (number % i) == 0:
            # Determine whether to add 1 or 2 to the divisor number
            if int(number/i) < limit:
                divisors += 1
            else:
                divisors += 2

    return divisors