# Write a program to input two numbers(A & B) from the user and print the maximum 
#element among A & B. 

A = int(input("Enter first number (A): "))
B = int(input("Enter second number (B): "))

if A > B:
    print("maximum number is:", A)
elif B > A:
    print("maximum number is:", B)
else:
    print("both numbers are equal")
