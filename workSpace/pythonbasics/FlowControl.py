# Python Flow Control

"""
 1. If Statement
 2. If Else statement
 3. If Elif Else statement
 4. For Loops
 5. While loops
 6. Nested Loops
 7. Break statement
 8. Continue Statement
 9. Loops with Else block
 10. Pass statement


"""


"""
 1. If statement  - If the condition is True, python will run the code present in If block, 
 otherwise it will skip the IF block

"""


a = 20
b = 30

if a > b:
    print(a)
    print("A is greater")
else:
    print(b)
    print("B is greater")

marks = int(input("Enter Marks : "))
section = input("Enter the section - ")
if marks == 100:
    if section == "A":
        print("Brilliant class")
    grade = "A+"
    print(grade)
elif 80 < marks < 100:
    print("B")
elif 60 < marks < 80:
    print("C")
else:
    print("Student is failed")