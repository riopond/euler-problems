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
                  15: 'fifteen', 16: 'sixteen', 17: 'seventeen', 
                  18: 'eighteen', 19: 'nineteen', 20: 'twenty', 30: 'thirty',
                  40: 'forty', 50: 'fifty', 60: 'sixty', 70: 'seventy', 
                  80: 'eighty', 90: 'ninety'}

# Variable to store the result
sum = 0

# Loop through every digit that needs to be checked
for i in range(1, maximum + 1):
    # Optionally, print out the following string to see the digit as
    # words (no spaces included)
    extended_num = ''
    hundreds, tens, ones = 0, 0, 0

    current = i

    # Check if i is the largest number possible in this program, 1000
    if current == 1000:
        sum += len('onethousand')
        continue

    if current >= 100:
        hundreds = int(current / 100)
        current -= hundreds * 100

    if current >= 20:
        tens = (int(current / 10)) * 10
        current -= tens

    ones = current

    # Craft the string
    if hundreds > 0:
        extended_num += num_words[hundreds] + 'hundred'
        if tens or ones > 0:
            extended_num += 'and'
    if tens > 0:
        extended_num += num_words[tens]
    if ones > 0:
        extended_num += num_words[ones]

    sum += len(extended_num)

# Output the result to the user
print(f"The sum of all letters in the numbers ranging from 1 to {maximum} is:")
print(sum)