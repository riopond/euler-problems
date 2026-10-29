# Problem 20:
#   n! means n * (n - 1) * ... * 3 * 2 * 1.

#   For example, 10! = 10 * 9 * ... * 3 * 2 * 1 = 3628800, and the sum 
#   of the digits in the number 10! is 
#   3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.

#   Find the sum of the digits in the number 100!.


# Store the desired factorial value. Can be changed by users.
factorial = 100

# Create variables to hold the calculated values
factorial_result = 1
result_sum = 0

# Loop through until every value is multiplied.
for i in range(1, factorial + 1):
    factorial_result *= i

# Save the trouble of constantly calling str() in the for loop.
stringed_result = str(factorial_result)

# Add each of the digits to the sum variable.
for i in range(0, len(stringed_result)):
    result_sum += int(stringed_result[i])

# Output the result to the user.
print(f"The sum of the digits resulting from {factorial}! is:")
print(result_sum)