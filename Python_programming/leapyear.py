year = int(input("Enter the year: "))

if(year % 400 == 0) and (year % 100 == 0):
    print("this year is leap year")
elif(year % 4 == 0) and (year % 100 != 0):
    print("this year is leap year")
else:
    print("this is not a leap year")
