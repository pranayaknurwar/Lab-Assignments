hardness = float(input("Enter hardness: "))
carbon = float(input("Enter carbon content: "))
tensile = float(input("Enter tensile strength: "))

cond1 = hardness > 50
cond2 = carbon < 0.7
cond3 = tensile > 5600

if cond1 and cond2 and cond3:
    grade = 10
elif cond1 and cond2:
    grade = 9
elif cond2 and cond3:
    grade = 8
elif cond1 and cond3:
    grade = 7
elif cond1 or cond2 or cond3:
    grade = 6
else:
    grade = 5


print("Grade of steel:", grade)