print("======Largest Three Number======")
a=int(input("enter the first number"))
b=int(input("enter the second number"))
c=int(input("nter the third number"))
if(a>=b and a>=c ):
    print("a is greater than b and c",a)
elif(b>=a and b>=c):
    print("b is grater than a and c",b)
else:
    print("c is grater than a and b",c)