print("====prime number range==== ")
start=int(input("Enter the starting number"))
end=int(input("Enter the last number"))
for i in range(start,end+1):
    count=0
    for n in range(1,i+1):
        if i%n==0:
            count+=1
    if count==2:
        print(n,end="\n")
                
            
