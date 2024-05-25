"""
Dictonary:
  Key and value pair
   1: Key - Numbers, String, Tuple
   2: Value - Python Object


"""

D1 = {

    "Name": "Rahul",
    "Age": 35

}

print(type(D1))
print(D1)

D2 = {

    "Name": "Rahul",
    "Age": 35,
    "Salary": 100000.10,
    "Organization": "Way2Automation",
    "Is_Married": True

}



print("Name - {}".format(D2["Name"]))
print("Age - {}".format(D2["Age"]))
print("Salary - {}".format(D2["Salary"]))
print("Organization - {}".format(D2["Organization"]))
print("Is_Married - {}".format(D2["Is_Married"]))


"""
Update key values in a Dictonary

"""


#D2["Name"] = input("Enter Name -- ")

#D2["Age"] = int(input("Enter Age -- "))

#D2["Salary"] = float(input("Enter Salary -- "))

#D2["Organization"] = input("Enter Organization -- ")

#D2["Is_Married"] = bool(input("Are you married -- "))

del D2["Is_Married"]

print(D2)




#Iterate a Dictionary


#printing all key values

for a in D2:
    print(a)


#printing all values

for b in D2:
    print(D2[b])


print("----------")


for c in D2.values():
    print(c)


for d in D2.items():
    print(d)


item={

    "fruits":["Apple","Mango","Banana"],
    "Price":100,
    "Size":10.5

}


print(item["fruits"][0])

item1={

    "location": "India",
    "fruits": {"Name": "Apple", "Price": 100}


}

print(item1["fruits"]["Name"])

print(item1.get("fruits").get("Price"))

print(len(item1))

print(item1.keys())