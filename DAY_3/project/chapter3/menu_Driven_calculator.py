print("======MENU DRIVEN CALCULATOR=======")
print("1.Addition")
print("2.substraction")
print("3.multiplicatin")
print("division")
choice=int(input("enter your chelif choice(1-4):"))
num1=float(input("Enter first number:"))
num2=float(input("Enter second number:"))
if choice==1:
    print("Result=",num1+num2)
elif choice==2:
    print("Result=",num1-num2)
elif choice==3:
    print("Result=",num1*num2)
elif choice==4:
    if num2!=0:
        print("Result=",num1/num2)
    else:
        print("Division by zero is not is not possible:")
else:
    print("invalid chioce:")
    