print("=========BMI calculator========")
weight=float(input("Enter your weight(kg):"))
height=float(input("Enter your height(meters):"))
bmi=weight/(height**2)
print("\n-------Result------")
print("your BMI is:",round(bmi,2)) #round(bmi,2) bmi ko 2 demical places tak round karta hai
if bmi<18.5:
    print("category:under weight")
elif bmi<18.5:
    print("category:normal weight")
elif bmi<25:
    print("category:over weight")
else:
    print("category:obese")
