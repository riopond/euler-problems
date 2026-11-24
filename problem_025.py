# Problem 25:
#   The Fibonacci sequence is defined by the recurrence relation:
#   F_n = F_{n - 1} + F_{n - 2}, where F_1 = 1 and F_2 = 1.

#   Hence the first 12 terms will be:
#       F_1 = 1
#       F_2 = 1
#       F_3 = 2
#       F_4 = 3
#       F_5 = 5
#       F_6 = 8
#       F_7 = 13
#       F_8 = 21
#       F_9 = 34
#       F_10 = 55
#       F_11 = 89
#       F_12 = 144

#   The 12th term, F_12, is the first term to contain three digits.

#   What is the index of the first term in the Fibonacci sequence 
#   to contain 1000 digits?


# Values to store Fibonacci sequence numbers used for calculation
first = 1
second = 1

# Adjustable value for desired number of digits/length of sequence num
digits = 1000

# Keep track of the index starting with number 2
# AKA the last known Fibonacci number from our given values
index = 2

# Loop until the solution is found
while len(str(second)) < digits:
    index += 1
    current = first + second

    # Update the values of (index - 2) and (index - 1)
    first = second
    second = current

# Output the result to the user.
print(f"Index {index} has a length of {digits}.")
print(f"The exact value is: {second}")