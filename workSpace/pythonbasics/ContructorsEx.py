"""

Constructors:

They are called as a first function of the class

syntax: __init__()

All classes have this function which is always executed when the class is being
initiated or an Object of the class is created


"""

class Practice:
    def __init__(self):
        print("Inside Constructor")

    def add(self):
        print("Adding something")


a = Practice()
a.add()



class Emp:
    def __init__(self,name,id):
        self.name = name
        self.id = id


    def display(self):
        print("Name is : ",self.name)
        print("ID is : ", self.id)


e = Emp("Rahul",101)
e.display()


f = Emp("Raj",102)
f.display()