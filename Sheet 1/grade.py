# Accept the percentage from the user and display the grade according to the following 
# criteria. 
# ● 
# Below 25 – D 
# ● 
# 25 to 45 – C 
# ● 
# 45 to 65 – B 
# ● 
# 65 to 85 – A 
# ● 
# Above 85 – A+ 
percentage = float(input("Enter your percentage: "))
if percentage >= 85:
    grade = "A+"
elif percentage >= 65:
    grade = "A"
elif percentage >= 45:
    grade = "B"
elif percentage >= 25:
    grade = "C"
else:
    grade = "D"
print("Your grade is:", grade)