"""
SET:
 1. It is similar to List
 2. It can store different type of values (Objects) String, Int, Float, Bool etc
 3. Set cannot have duplicate values
 4. Set are defined {}
 5. It's a collection which is unordered and unindexed
"""

S1 = {"Selenium","Appium","Cypress",100,True,100.1,"Selenium"}

print(S1)
print(type(S1))
print(len(S1))


for i in S1:
    print(i)

S1.add("Protractor")

print(S1)

S1.discard("Cypresssdff")

print(S1)

S2 = {"Hello"}
#print(S1 + S2)

S3 = S1.copy()

print("----printing S3---")
S1.clear()
print(S3)
print(S1)