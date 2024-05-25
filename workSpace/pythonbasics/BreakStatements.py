"""
Break - It is used to Break the current loop and resume the other code

"""

for i in range(10):
    if i==7:
        print("Executing break at ",i)
        break
    print("Printing the value as ",i)

print("Outside the for loop")

"""
Continue statement

    It is used to skip the current Iteration and contine with the next Iteration


"""

print("--------Printing Odd numbers---------")


for i in range(10):
    if i%2 ==0:
        print("Even number is ",i)
        continue
    print("Odd numbers is : ",i)



print("---------")


for i in range(10):
    if i==7:
        print(i)
        break
    elif i==5:
        continue
    print(i)


"""
Else block within the loops

"""
print("----Else Block-----------")


cart = [10,20,600,30,40,50,550]

for item in cart:
    if item>500:
        print("This item is not allowed")
        continue
    print(item)
else:
    print("All items are successfully processed..")


for x in "Rahul":
    pass