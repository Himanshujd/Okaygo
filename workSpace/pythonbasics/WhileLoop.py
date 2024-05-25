"""

while condition/true
    execute the block

"""
i=0
while i<10:
    print("Hello")
    i += 1


# sum of first n numbers


n = int(input("Enter the number :"))


sum = 0
i = 1
while i<=n:
    sum = sum+i
    i = i+1


print("Sum is {}".format(sum))