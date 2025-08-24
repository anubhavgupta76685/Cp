n=int(input("enter a number"))
d=0
n1=n
rev=0
while n>0:
    d=n%10
    n=n//10
    rev=rev*10+d
if rev==n1:
    print("entered number is palindrome")
else:
    print("entered number is not palindrome")