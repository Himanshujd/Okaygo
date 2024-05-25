print(type("This is a String"))

a="Welcome to W2A"
print(a)

b='Welcome to W2A'
print(b)

'''

Hey, My name is "Rahul"

'''

print('Hey, My name is "Rahul"')


e = "Hey" \
    "My name is" \
    "Rahul"


print(e)


g = """

Hey
My Name is:
Rahul



"""

print(g)


print("This is Rahul's \"New\" house")


name="Rahul"

print(name[1:4:2])
print(name[::-1])

print(len(name))

abc = "Hello, Rahul"





print(abc.strip())


print(name.lower())


print(name.upper())


b = abc.split(",")
print(b[1].strip())


ab = "Hi"
cd = " Way2Automation"

print(ab+cd)


print("10"+"10")


a="10"*4
print(a)

print("ba"+"na"*2)


city="New Delhi"

print("Hey, I live in ",city)

# f-Strings
# format()
# %
Age=35
id=10.12

print(f"Hey, I live in {city}, My Age is {Age} and id is {id}")


print("Hey, I live in {}, My Age is {} and id is {}".format(city,Age,id))


print("Hey, I live in %s, My Age is %d and id is %f"%(city,Age,id))