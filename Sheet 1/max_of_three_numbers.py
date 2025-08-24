 # Write a program to input three numbers(A, B & C) from the user and print the 
# minimum element among A, B & C. 
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))
if a > b and a > c:
    print("maximum number is:", a)
elif b > a and b >c:
    print("maximum number is:", b)
else:
    print("The maximum number is:",c)
