# Problem 4:
#   A palindromic number reads the same both ways.
#   The largest palindrome made from the product of two 2-digit
#   numbers is:
#   9009 = 91 * 99.

#   Find the largest palindrome made from the product of 
#   two 3-digit numbers.


from analyser import numPalindromeFinder

# List to keep track of all found palindromes
palindromes = []

# Reversing the range makes it so the range descends from the stop
# to the start
for one in reversed(range(100, 1000)):
    for two in reversed(range(100, 1000)):
        product = str(one * two)
        # By checking the two ends of the number are the same, reduces
        # number of times the function is called
        if product[0] == product[-1]:
            if(numPalindromeFinder(product)):
                palindromes.append(int(product))

# Sort the numerical products from least to greatest
palindromes.sort()

# Output the result to the user
print(f"The greatest product found is: ")
print(palindromes[-1])