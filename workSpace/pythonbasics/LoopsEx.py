"""
Iterative Statements:
 1. For Loop
 2. While Loop

"""

"""

For Loop -->
    
    For every x, in the sequence to perfom some activity, which means every element which is avaiable
    in the sequence, range, list, tuple or a dictionary
    
    Syntax:
    
    for x in sequence:
        statements

"""


sequence = "Rahul"
i=0
for x in sequence:
    print("The character preset at {}, index - {}".format(i,x))
    i=i+1

for x in range(10): #0-n-1: 0 to 9
    print("Way2Automation ",x)

for x in range(2,30,3):
    print(x)

n = int(input("Enter the number :"))

for x in range(1,11):
    print(n,"*",x,"=",n*x)



List = eval(input("Enter the numbers for addition : "))

sum = 0
for x in List:
    sum = sum+x
print("The Sum is : ",sum)


string = "My Name is Rahul"

s = string.split(" ")

for x in s:
    print(x)