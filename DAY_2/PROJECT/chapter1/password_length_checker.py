print("=======Password length checker======")
password=input("enter the pasword:")
length=len("password")
print("password length:",length)
if length>=8:
    print("strong password length")
else:
    print("weak password(minimum 8  character reuired)")