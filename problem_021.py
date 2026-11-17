# Problem 21:
#   Let d(n) be defined as the sum of proper divisors of n (numbers less 
#   than n which divide evenly into n).

#   If d(a) = b and d(b) = a, where a != b, then a and b are an amicable
#   pair and each of a and b are called amicable numbers.

#   For example, the proper divisors of 220 are 
#   1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; therefore, d(220) = 284.
#   The proper divisors of 284 are 
#   1, 2, 4, 71 and 142; so d(284) = 220. 

#   Evaluate the sum of all amicable numbers under 10000.


from analyser import sumDivisorFinder

# Adjustable integer to store the list limit
limit = 10_000
numbers = [i for i in range(1, limit)]

# List to store all amicable numbers
amicable = []

# Sum of the amicable numbers
amicable_sum = 0

# Analyse each of the numbers of the list
while numbers:
    a = numbers.pop()
    b = sumDivisorFinder(a, True)

    # If there are no other divisors besides 1 and itself, disregard
    if b == 1:
        continue

    # Check to see what d(b) is
    c = sumDivisorFinder(b, True)

    # Check for 
    #   d(a) = b
    #   d(b) = a
    #   a not b
    if c == a and b != a:
        amicable.append(a)
        amicable.append(b)

        # Prevent a repeat of the already-checked integer b
        numbers.remove(b)

amicable_sum += sum(amicable)

# Output result to the user
print(f"The sum of all amicable numbers under {limit} is:")
print(int(amicable_sum))