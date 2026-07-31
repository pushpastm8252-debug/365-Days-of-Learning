print("======= prime number checker=======")
n=int (input("enter the number:"))
if n<=1:
    print("not a prime number")
else:
    isprime=True
    for i in range(2,n):
        if n%i==0:
            isprime=False
            break
        if isprime:
            print("Prime Number")
        else:
            print("Not a prime number")