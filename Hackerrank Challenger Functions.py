# Write Function Problem Hackerrank Challenge

# Given a year determine if it is a leap year or not. If leap year return Boolean True other return False
# In the Gregorian calendar, three conditions are used to identify leap years:
# The year can be evenly divided by 4, is a leap year, unless:
# The year can be evenly divided by 100, it is NOT a leap year, unless:
# The year is also evenly divisible by 400. Then it is a leap yea


def leap(year):
    leap = False
    if year % 4 == 0:
        if year % 100 == 0:  # if year is evenly divisible by 100, then NOT leap year, else true
            if year % 400 == 0:  # if the year is evenly divisible by 400, then leap year, else false
                return True
            else:
                return False
        else:
            return True
    else:
        return False

year = int(input("Enter Year "))
print(leap(year))

# Notes : Code can be better and does not require as much as I do
# From Another User
"""
def is_leap(year):
    leap = False
    if year % 4 == 0:
        leap = True
        if year % 100 == 0:
            leap = False
            if year % 400 == 0:
                leap = True
    return leap
year = int(input("Enter Year:"))
print(is_leap(year))
"""
