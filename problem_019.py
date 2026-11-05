# Problem 19:
#   You are given the following information, but you may prefer to do 
#   some research for yourself.

#       1 Jan 1900 was a Monday.
#       Thirty days has September, 
#       April, June and November.
#       All the rest have thirty-one,
#       Saving February alone,
#       Which has twenty-eight, rain or shine.
#       And on leap years, twenty-nine.
#       A leap year occurs on any year evenly divisible by 4, 
#       but not on a century unless it is divisible by 400.
   
#   How many Sundays fell on the first of the month during the 
#   twentieth century (1 Jan 1901 to 31 Dec 2000)?


# Initial date position
day = 2

# Variable to store the result
sundays = 0

for year in range(1, 101):
    for month in range(1, 13):
        # Check to see if the first day is a Sunday
        if day == 7:
            sundays += 1
        # During 30-day months, day position moves up 2
        if month in [4, 6, 9, 11]:
            day += 2
        # During 31-day months, day position moves up 3
        elif month in [1, 3, 5, 7, 8, 10, 12]:
            day += 3
        # During leap years, day position moves up 1 in February
        elif month == 2:
            if (year % 4) == 0:
                day += 1

        # Day position can only be in the range of 1 to 7
        if day > 7:
            day -= 7

# Output the result to the user
print("From 1901-2000, there are this many Sundays on the first of the month:")
print(sundays)