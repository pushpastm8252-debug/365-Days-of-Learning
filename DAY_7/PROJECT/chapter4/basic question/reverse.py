print("==== Reverse number=====")
n=int(input("Enter the number:"))
reversed=0
while n>0:
    digit=n%10
    reversed=reversed*10+digit
    n=n//10
    print("reverse=",reversed)