print("========Simple interest calculator=======")
p=int(input("Enter the principle number"))
t=int(input("Enter the time number"))
r=int(input("Enter the rate time"))
si=(p*r*t)/100
total_amount=p+si
print("simple intrest=",si)
print("total_amount=",total_amount)