#Python Operators



""""

1. Arithmetic
2. Comparison
3. Equality
4. Logical
5. Bitwise
6. Shift
7. Assignment
8. Ternary
9. Membership
10. Identity

"""

"""
1. Arithmetic Operators
  a. Addition
  b. Subtraction
  c. Multiplication
  d. Division
  e. Modulus (%)
  f. Exponential Operator (**)
  g. Floor Division (//)


"""

a=10
b=5

print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a%b)
print(a**b)
print(a//b)

"""

2. Comparison Operators

    a. Greater than (>)
    b. Greater than equal to (>=)
    c. Less than (<)
    d. Less than equal to (<=)

"""


a=10
b=5

print(a>b)
print(a>=b)
print(a<b)
print(a<=b)


s1="Cat" #67
s2="Dog" #68
print("------------")
print(s1>s2)
print(s1>=s2)
print(s1<s2)
print(s1<=s2)

print(ord("C"))

print(ord("D"))


print('apple'>'apple')

print('apple'>='apple')

print('apple'<'apple')

print('apple'<='apple')

# Relational Operator Chaining

print(10<20<30<40)


"""

3. Equality Operators
    a. Equal to (==)
    b. Not Equal to (!=)

"""

print("-----Equality Operators-----")

a=10
b=20
print(a==b)
print(a!=b)

print("--------------")

print(1==True)
print(0==True)
print(0==False)
print(10==10.0)
print("Way2Automation" == "Way2Automation")


"""

4. Logical Operators

    a. And --> Return true whenever both the arguments are true in nature
    b. Or --> Return true, if atleast one argument is True
    c. Not --> return the reverse

"""


print("---Logical Operators---")


print(True and True)
print(1 and 0)


"""
  a. if the value x, evaluates to False, then the result is the value x
  b. if the value x, evaluates to True, then the result is the value y


"""


print(10 and 20)
print(0 and 20)


print(10 or 20)
print(0 or 10)


# username = input("Enter the username : ")
# password = input("Enter the password: ")
#
# if username=="way2automation" or password=="test":
#     print("Valid user")
# else:
#     print("Invalid user")

print(not True)
print(not False)


a=10


print(not a==10)

"""

5. Bitwise Operators
    a. Bitwise And (&)
    b. Bitwise Or (|)
    c. Bitwise XOR (^)
    d. Bitwise complement (~) - -(n+1)


"""


print("------Bitwise &----")

print(bin(16))
print(bin(18))
print(16 & 18)

print(16 | 18)

print(16^18)
print(0b00010)
print(~(-4))


"""
6. Shift Operators

    a. Left shift (<<)
    b. Right shift (>>)


"""

print(bin(10))
print(0b101000)
print(10<<2)
print(bin(2))
print(10>>2)

"""

7. Assignemnt Operator

    =, +=, -=, *= etc
"""


print('-------------assignment operators-------')

x=20
print(x)
x += 10 # x = x + 10; x = 20+10
print(x)
x *=10
print(x)
x -=10
print(x)

# python does not support Increment / Decrement operators
#print(x++)


"""

8. Ternary Operators

    It is a Conditional operator
    There is no specific keyword for Ternary Operator
    Var = First value if condition Else second value

"""


a = 50
b = 20
c = 30 if a>b else 40
print(c)

a = int(input("Enter a = "))
b = int(input("Enter b = "))
min = a if a<b else b
print(min)


"""
9. Identity Operators
   1. is
   2. is not
   
   a is not b, return true only when two reference var are pointing to the same object
   
"""

a = 10
b = 10
print(a is b)
print(a is not b)


"""
10. Membership Operator
  1. in
  2. not in

"""


a = [10,20, 30, 55, "abcd"]

print(10 in a) #true
print(20 not in a ) #false
print(21 not in a) #true
print(22 in a) #false