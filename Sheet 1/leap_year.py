# WAP to check whether a year is a leap year or not
year = int(input("Enter a year: "))
# Leap year conditions:
if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
    print(year, "is a leap year")
else:
    print(year, "Not a leap year")
