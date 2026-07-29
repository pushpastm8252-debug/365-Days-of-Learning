print("====ATM PIN verification====")
pin=153659
user_pin=int(input("Enter the number:"))
if user_pin==pin:
    print("the correct pin:",user_pin)
else:
    print("The incorrect:",user_pin)