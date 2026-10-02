# Problem 10:
#   The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

#   Find the sum of all the primes below two million.


from analyser import primeFinder

# Initialise with two early known primes
num = 3
sum = 2

# Create a variable that can be edited to the user's needs
limit = 2_000_000

while num <= limit:
    if primeFinder(num):
        sum += num
        print(f"{sum} sum, {num} current num")

    # Increment to the next odd number every iteration
    num += 2

# Print the result to the user.
print(f"The sum of all primes under {limit} is: {sum}")