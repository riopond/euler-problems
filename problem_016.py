# Problem 16:
#   2^15 = 32768 and the sum of its digits is:
#   3 + 2 + 7 + 6 + 8 = 26.

#   What is the sum of the digits of the number 2^1000 ?


# User can choose the desired exponent value
exponent = 1000

# Variables to hold calculated integers
power = pow(2, exponent)
sum = 0

# Run through every digit in the resulting power
for i in str(power):
    sum += int(i)

# Print the result to the user
print(f"The sum of the digits in 2^{exponent} is:")
print(sum)