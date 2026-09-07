# Problem 5:
#   2520 is the smallest number that can be divided by each of the 
#   numbers from 1 to 10 without any remainder.

#   What is the smallest positive number that is evenly divisible 
#   by all of the numbers from 1 to 20?


factor = 19
found = False

while not found:
    multiple = 20 * factor

    for i in range(3, 19):
        if (multiple % i) != 0:
            factor += 1
            break
        elif i == 19:
            found = True

print(f"The result is: {multiple}")