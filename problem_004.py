# Problem 4:
#   A palindromic number reads the same both ways.
#   The largest palindrome made from the product of two 2-digit
#   numbers is:
#   9009 = 91 * 99.

#   Find the largest palindrome made from the product of 
#   two 3-digit numbers.


def palindromeFinder(number):
    """ A function designed to find palindromes of specifically 
    integer values, returning True if the number is a palindrome 
    and False otherwise. """
    numString = str(number)
    length = len(numString)

    # Numbers with only one digit are palindromes
    if length == 1:
        return True

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

number = input("Insert a test number to check for palindromes: ")
print(palindromeFinder(number))