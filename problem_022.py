# Problem 22:
#   Using 0022_names.txt, a 46K text file containing over five-thousand
#   first names, begin by sorting it into alphabetical order.
#   Then working out the alphabetical value for each name, multiply
#   this value by its alphabetical position in the list to obtain a
#   name score.

#   For example, when the list is sorted into alphabetical order,
#   COLIN, which is worth 
#   3 + 15 + 12 + 9 + 14 = 53, 
#   is the 938th name in the list. 
#   So, COLIN would obtain a score of 938 * 53 = 49714.

#   What is the total of all the name scores in the file?


# Read in data from the data file. Custom data can be used in the file.
file = open('data/0022_names.txt')
data = file.read().split(',') # The data must be manually split
data = [word[1:-1] for word in data] # Quotation marks removed
data.sort()

# Dictionary defining every letter and their value
letters = {'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5, 'F': 6, 'G': 7, 
            'H': 8, 'I': 9, 'J': 10, 'K': 11, 'L': 12, 'M': 13, 'N': 14,
            'O': 15, 'P': 16, 'Q': 17, 'R': 18, 'S': 19, 'T': 20, 
            'U': 21, 'V': 22, 'W': 23, 'X': 24, 'Y': 25, 'Z': 26}

# Store the sum/result
list_sum = 0

for name in range(0, len(data)):
    name_value = 0
    # Calculate the numerical value of each name
    for char in data[name]:
        name_value += letters.get(char)

    # Multiply the value by the position in the list
    name_value *= name + 1

    # Add to the result
    list_sum += name_value