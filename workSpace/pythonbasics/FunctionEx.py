"""

Functions:
    1. Block of code used to perform a specific action
    2. Reusable Block
    3. Can have parameters
    4. Collection of multiple functions create a program
    5. Pre defined functions print() sort() etc

def function_name:
    statemnent / code to be executed

"""


def print_my_name():
    print("My Name is Rahul")

print_my_name()


def print_my_name_as(name):
    #print("My Name is : "+name)
    return "My Name is : "+name


name = print_my_name_as("Rahul Arora")
print(name)



def get_user_details(name,age,salary):
    print("Name is :",name," Salary is : ",salary," Age is ",age)

get_user_details("Rahul",35,100000)

get_user_details(name="Rahul",salary=100000,age=35)


"""
Types of Arguments:

    1. Required Arguments
    2. Keyword Arguments
    3. Default Arguments
    4. Variable length Arguments

"""


def req_arguments(a,b):
    print(a+b)


req_arguments(10,20)


def def_argument(name,school="Oxford"):
    print("Name - {}".format(name))
    print("School - {}".format(school))


def_argument("Rahul")
def_argument("Cory","DPS")



get_user_details(name="Rahul",salary=100000,age=35)


def var_argument(school,*name):
    print(school)
    for i in name:
        print(i)

var_argument("Oxford","Rahul","Cory","Tom","Selvan",12,2.2,True)