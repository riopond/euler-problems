# Problem 5:
#   2520 is the smallest number that can be divided by each of the 
#   numbers from 1 to 10 without any remainder.

#   What is the smallest positive number that is evenly divisible 
#   by all of the numbers from 1 to 20?


from analyser import primeFinder

# The dictionary will store the greatest power of each prime number
prime_factorisation = {}
multiple = 1

for i in range(2, 21):
    # The prime will first be stored as a dictionary key
    if primeFinder(i) == True:
        prime_factorisation[i] = 1
    # No prime greater than 3 will exceed power of 1 for range 1-20
    elif i % 3 == 0:
        power = 1
        quotient = i / 3
        # Keep looping until the final root is found
        while quotient % 3 == 0:
            power += 1
            quotient = quotient / 3
        if prime_factorisation[3] < power:
            prime_factorisation[3] = power
    elif i % 2 == 0:
        power = 1
        quotient = i / 2
        while quotient % 2 == 0:
            power += 1
            quotient = quotient / 2
        if prime_factorisation[2] < power:
            prime_factorisation[2] = power

for k, v in prime_factorisation.items():
    print(f"key: {k} value: {v}")
    multiple *= pow(k, v)

print(f"The result is: {multiple}")