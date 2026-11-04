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


for year in range(1, 100):
    for month in range(1, 13):
        if month in [4, 6, 9, 11]:
            print(f"This is for 30-day month {month} and year {year}")
        elif month in [1, 3, 5, 7, 8, 10, 12]:
            print(f"This is for 31-day month {month} and year {year}")
        elif month == 2:
            if (year % 4) == 0:
                print(f"Year {year} is a leap year, 29 days in Feb")