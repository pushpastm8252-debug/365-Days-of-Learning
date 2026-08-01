print("====largest digit of number=====")
n=int(input("Enter the number:"))
largest=0
while n>0:
    digit=n%10
    if digit>largest:
        largest=digit
        n=n//10
        print("largest",largest)