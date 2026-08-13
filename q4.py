#Take a year as input and check if it's a leap year.
year=int(input("enter a year : "))
if(((year%4==0 and year%100!=0) or  year%400==0)):
    print("its a leap year : ", year)
else:
    print("not a leap year")
