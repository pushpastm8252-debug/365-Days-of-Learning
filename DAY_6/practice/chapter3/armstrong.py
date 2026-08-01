print("=====Armstrong number======")
n=int(input("Enter the number"))
temp=n
sum=0
while temp>0:
    digit=temp%10
    sum=sum+digit**3
    temp=temp//10
if sum==n:
    print("Armstrong")
else:
    print("not armstrong")