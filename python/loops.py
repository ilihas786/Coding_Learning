# two dimensional loops

n=int(input("Enter the value of n"))

for i in range(n):
    for j in range(n):
        print("*",end="")
    print()
    
for i in range(n+1):
    for j in range(i):
        print(j+1,end=" ")
    print()