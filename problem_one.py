# Problem 1:
#   If we list all the numbers below 10 that are multiples of 3 or 5, 
#   we get 3, 5, 6, and 9. The sum of these multiples is 23.
# 
#   Find the sum of all the multiples of 3 or 5 below 1000.


# Lists of multiples relevant to this problem
threes = list(range(3, 1000, 3))
fives = list(range(5, 1000, 5))

# Loop through the lists and remove duplicate multiples from the fives list
for n in threes:
    for m in fives:
        if n == m:
            fives.remove(m)

# Using the sum() method, add all elements from the two lists
multiplesSum = sum(threes) + sum(fives)

# Output the result to the user
print("The sum of all multiples of 3 and/or 5 are: ")
print(multiplesSum)