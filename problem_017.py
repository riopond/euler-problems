# Problem 17:
#   If the numbers 1 to 5 are written out in words: 
#   one, two, three, four, five, then there are 
#   3 + 3 + 5 + 4 + 4 = 19 letters used in total.

#   If all the numbers from 1 to 1000 (one thousand) inclusive were 
#   written out in words, how many letters would be used?

#   NOTE: Do not count spaces or hyphens. For example, 
#   342 (three hundred and forty-two) contains 23 letters and 
#   115 (one hundred and fifteen) contains 20 letters. 
#   The use of “and” when writing out numbers is in compliance 
#   with British usage.


# Customisable integer to store the desired max number.
# Cannot go beyond 1000.
maximum = 1000

num_words = {1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five',
                  6: 'six', 7: 'seven', 8: 'eight', 9: 'nine', 10: 'ten',
                  11: 'eleven', 12: 'twelve', 13: 'thirteen', 14: 'fourteen',
                  15: 'fifteen', 16: 'sixteen', 17: 'seventeen', }

# Variables to store the results
sum = 0

for i in range(1, maximum + 1):
    extended_num = ''
    if i == 1000:
        extended_num = 'onethousand'

    sum += len(extended_num)

# Output the result to the user
print(f"The sum of all letters in the numbers ranging from 1 to {maximum} is:")
print(sum)