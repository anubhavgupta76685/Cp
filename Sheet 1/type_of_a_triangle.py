#Read three angles of triangles and determine their types(Right triangle, Obtuse triangle, Acute triangle)
a = int(input("Enter first angle: "))
b = int(input("Enter second angle: "))
c = int(input("Enter third angle: "))
if a + b + c == 180 and a > 0 and b > 0 and c > 0:
    if a == 90 or b == 90 or c == 90:
        print("It is a Right Triangle.")
    elif a > 90 or b > 90 or c > 90:
        print("It is an Obtuse Triangle.")
    else:
        print("It is an Acute Triangle.")
else:
    print("The angles do not form a valid triangle.")
