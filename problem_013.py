# Problem 13:
#   Work out the first ten digits of the sum of the provided one-hundred 
#   50-digit numbers. 

# Read in data from the data file. Custom data can be used in the file.
file = open('data/problem_013_data')
data = file.read().split('\n') # The data must be manually split

# Initialise an integer to store the sum
sum = 0

# Iterate through each item in the list
for current in data:
    sum += int(current)

# Output the result to the user
print("The sum of the data is:")
print(sum)