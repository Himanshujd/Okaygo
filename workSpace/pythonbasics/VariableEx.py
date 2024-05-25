class Dog:

    legs = 4

    def __init__(self):
        self.name = "Milo"
        self.color = "Brown"

    def getDogName(self):
        print(self.name)

    @classmethod
    def getLegsCount(cls):
        print(cls.legs)

    @staticmethod
    def generalInformation():
        print("Beware of Dogs")


d1 = Dog()
d2 = Dog()

d2.name = "Bruno"
d2.color = "White"

Dog.legs = 3

print(d1.name,d1.color,Dog.legs)
d1.getDogName()
Dog.getLegsCount()

Dog.generalInformation()


print(d2.name,d2.color,Dog.legs)


"""
3 types of Methods / functions

1. Instance Method - Use to access instance variable of the class
2. Class Method - Use to access static of the class
3. Static Method - Standalone method


"""


