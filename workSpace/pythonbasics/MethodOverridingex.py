"""

3. Method Overriding


"""


class MethodOverridingBase:

    def __init__(self):
        print("base class")

    def a(self):
        print("inside Base class")


class MethodOverridingDerived(MethodOverridingBase):

    def __init__(self):
        super().__init__()
        print("Child class")


    def b(self):
        print("something")
    def a(self):
        super().a()
        print("Inside Derived class")


obj1 = MethodOverridingDerived()
obj1.a()