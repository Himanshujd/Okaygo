"""

OOPS Concepts / Procedural language (Step by Step implementation of the code)

    1. Classes
    2. Objects
    3. Encapsulation
    4. Absraction
    5. Inheritance
    6. Polymorphism


    kgkjsfd
    lkhsdfkjs
    jhsdgfsjkdfs
    jsdhgfsfjks

        kgkjsfd
    lkhsdfkjs
    jhsdgfsjkdfs
    jsdhgfsfjks


What is a Class?


1. A Class can be defined as a Blueprint / Template which describes the state / behavior
of it's object


class <classname>:
    statements


    School Class:
    Name
    Age
    Roll number
    Address

    1 - Rahul, 16, 1, asfsdf
    2. Raman, 18, 2, asfsdfser

"""

class Human:
    eyes = "blue"
    nose = "Large"

    def eyes_function(self,color):
        print("This is a function to see - {}".format(color))

    def noes_function(self,size):
        print("This is a function to smell - {}".format(size))

    def ear_function(self,color):
        print("This is a function to hear - {}".format(color))


a = Human()

a.eyes_function("Black")
a.ear_function("Brown")
a.noes_function("Small")


b = Human()

b.eyes_function("Blue")
b.ear_function("White")
b.noes_function("Large")