# Problem 7:
#   By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, 
#   we can see that the 6th prime is 13.

#   What is the 10,001st prime number?


from analyser import primeFinder

# Setting up this integer gives the user freedom to alter the problem
requested_prime = 10001

# List that will store all found prime values up to requested
prime_numbers = []

# Start the prime number search from 2
current = 2

while len(prime_numbers) != requested_prime:
    if primeFinder(current):
        prime_numbers.append(current)

    current += 1

# Output the result to the user
print(f"The {requested_prime} position prime value is: ")
print(prime_numbers[-1])