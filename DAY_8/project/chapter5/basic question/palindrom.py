print("====palindrom====")
n=int(input("Enter the number:"))
reverse=0
temp=n
while n>0:
    digit=n%10
    reverse=reverse*10+digit
    n=n//10
if temp==reverse:
    print("palindrom")
else:
    print("not palindrom")
