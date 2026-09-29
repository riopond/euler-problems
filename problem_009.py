# Problem 9:
#   A Pythagorean triplet is a set of three natural numbers, a < b < c,
#   for which:
#   a^2 + b^2 = c^2

#   For example, 
#   3^2 + 4^2 = 9 + 16 = 25 = 5^2

#   There exists exactly one Pythagorean triplet for which 
#   a + b + c = 1000.
#   Find the product abc.


import math

# Adjustable goal sum for users to choose their own value
goal_sum = 1000

for a in range(1, goal_sum):
    for b in range(a+1, goal_sum):
        c = math.sqrt(pow(a, 2) + pow(b,2))

        if (a+b+c) == goal_sum:
            # Result found, print to the user
            print(f"The three values are: {a} {b} {c}")
            print(f"The product is: {a*b*c}")
        elif (a+b+c) > goal_sum:
            break