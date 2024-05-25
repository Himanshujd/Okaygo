"""

Tuples
 1. It is used to store the sequence of IMMUTABLE Objects
 2. Mostly all the other operations are similar to a List

"""


T1 = ("Rahul",12,1.45)
print((type(T1)))

#T1[2]=20

print(T1)


"""
Tuple slicing / Indexing

"""


T2 = (0,1,2,3,4,5)


print(T2[0:]) # 0,1,2,3,4,5
print(T2[:]) # 0,1,2,3,4,5
print(T2[2:4]) # 2,3
print(T2[1:3]) #1,2
print(T2[:4]) #0,1,2,3


#del T2[3]

print(T2)

"""
Tuple Operations:
    1. Repetation
    2. Concatenation
    3. Membership Operation
    4. Iteration

"""


T3 = (1,"Rahul")
print(T3 * 2)


T4 = (2,"Cory")
print(T3 + T4)

print("Rahul" in T3)

print("Cory" not in T4)


for i in (1,2,3,4,5):
    print(i)