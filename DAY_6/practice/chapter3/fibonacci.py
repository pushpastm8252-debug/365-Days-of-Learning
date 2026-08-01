print("=======Fibonacci Series=======")
n=int(input("enter how many terms:"))
a=0
b=1
for i in range(n):
    print(a,end="")
    c=a+b
    a=b
    b=c
    