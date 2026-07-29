print("=====System Logic System=====")
username=input("enter the username:")
password=int(input("Enter the number:"))
if username=="admin":
    if password=="1456":
        print("login succesfull:")
    else:
     print("incorrect password:")
else:
    print("invalid password:")