# Problem 6:
#   The sum of the squares of the first ten natural numbers is, 
#   1^2 + 2^2 + ... + 10^2 = 385.
#   The square of the sum of the first ten natural numbers is, 
#   (1 + 2 + ... + 10)^2 = 55^2 = 3025.
#   Hence the difference between the sum of the squares of the first 
#   ten natural numbers and the square of the sum is  3025 - 385 = 2640.

#   Find the difference between the sum of the squares of the first 
#   one hundred natural numbers and the square of the sum. 


# Creating a problem range variable gives the user the freedom to
# alter the program to their needs.
problem_range = 100

square_of_sum = 0
sum_of_squares = 0

for current in range(1, problem_range+1):
    square_of_sum += current
    sum_of_squares += pow(current, 2)

square_of_sum = pow(square_of_sum, 2)

if sum_of_squares > square_of_sum:
    result = sum_of_squares - square_of_sum
else:
    result = square_of_sum - sum_of_squares

# Output the result to the user
print("The difference of the sum of squares and the square of the sum is: ")
print(result)