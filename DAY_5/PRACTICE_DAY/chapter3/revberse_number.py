print("=====Reverse number=====")
a=int(input("enter the number:"))
reverse=0
while a>0:
    digit=a%10 #last digit nikalo
    reverse=reverse*10+digit # reverse number me digit add kro
    a=a//10 # last digit nikalo
    print("reverse=",reverse)
    