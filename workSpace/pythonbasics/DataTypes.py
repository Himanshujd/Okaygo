"""
Datatypes:
    1. List
    2. Tuple
    3. Dictionary

"""

"""
List - Data type
 
 1. It is just a consecutive collection of related items / words
 2. Represents a group of values as a single entity, order is very important
 3. It allows duplicate values as well.
 4. It is represented by a square bracket []
 5. values are seprated by commas

"""

a = []  # empty list
b = [1, 2.3, "Rahul", True, 3 + 2j, "Rahul"]
print(type(b))
print(b)

"""

1. order is preserved

"""

print(b[2])

"""

2. List allows duplicate values

"""

print(b[5])

"""

3. List is Mutuable in nature

"""

b.append("Cory")

print(b)

emp = ["Rahul", 102, "India"]
Dep1 = ["ÏT", 10]
Dep2 = ["Elec", 11]

print(f"Name is {emp[0]}, Department is {emp[1]} and country is {emp[2]}")

"""

List Slicing

"""

c = [0, 1, 2, 3, 4, 5, 6]

print(c[0:])  # 0,1,2,3,4,5,6
print(c[:])  # 0,1,2,3,4,5,6
print(c[2:4])  # 2,3
print(c[:4])  # 0,1,2,3

"""
Updating List values

"""

d = [1, 2, 3, 4, 5, 6]

print(d)

d[3] = 7

print(d)

d[1:4] = ["Rahul", "Cory", 10]
print(d)

del d[4]
print(d)

e = ["a", "c", "e", "b", "d"]

print(e)
e.sort()
print(e)
e.sort(reverse=True)
print(e)


"""

List operations:

    1. Repetition operation
    2. Concatenation operation
    3. Memebership operation
    4. Iterations
    5. Length function


"""

print("----l1")
l1 = [1,2,3,"Rahul",True]

print(l1*2)


l2 = [5,6,7,"Cory",False]
print(l1 + l2)

print("Rahul" in l1)
print("Cory" not in l2)

for i in l1:
    print(i)

print(len(l2))


l3 = [1,2,3,4,5,7,9]

print(max(l3))
print(min(l3))


string = "Rahul"
print(list(string))