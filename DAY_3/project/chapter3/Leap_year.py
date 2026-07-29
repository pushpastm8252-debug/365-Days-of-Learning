print("======Leap Year======")
year=int(input("enter the leap year:"))
if((year%400==0) or (year%4==0) and (year%100!=0)):
    print("leap year",year)
else:
    print("this is not leap year",year)