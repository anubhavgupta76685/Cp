
n = int(input("enter a number"))
for i in range(n,0,-1 ):          
    for j in range(n - i):
        print("_", end="")     
    for k in range(i):
        print("* ", end="")    
    print()  