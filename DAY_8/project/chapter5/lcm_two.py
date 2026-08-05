print("=====Lcm of numbers======")
n=int(input("Enter the number:"))
m=int(input("Enter  the number:"))
lcm=max(n,m)
while True:
    if lcm %n==0 and lcm %m==0:
        print("LCM=",lcm)
        break
    lcm+=1
