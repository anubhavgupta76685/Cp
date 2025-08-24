# You are given 3 integer angles(in degrees), A, B, and C, of a triangle. You have to tell 
#whether the triangle is valid or not. A triangle is valid if the sum of its angles equals 
#180.

a=int(input("enter the first angle of a triangle"   ))
b=int(input("enter the second angle of a triangle"   ))
c=int(input("enter the third angle of a triangle"   ))

if (a+b+c == 180):
    print("its is valid triangfle")
else:
    print("triangle is not valid ")