# Problem 10:
#   The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

#   Find the sum of all the primes below two million.


from analyser import primeFinder

# Create a variable that can be edited to the user's needs
limit = 2_000_000

# Initialise with a full list of every number under the limit
num_list = list(range(2, limit))

for i in num_list:
    j = pow(i, 2)
    if j in num_list:
        num_list.remove(j)
    for k in range(j, limit):
        if (k%i) == 0 and (k in num_list):
            num_list.remove(k)

# Print the output to the user.
print(sum(num_list))