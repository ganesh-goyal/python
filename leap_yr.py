# given year is leap year or not 

year = int(input("enter the year:"))

if year % 4 ==0:
    print(" %d year is 'leap year'" %(year))
else:
    print("%d  is not a 'leap year' "%(year))
