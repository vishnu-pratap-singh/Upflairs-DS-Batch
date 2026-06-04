print("hello function")

def my_function(*number):
    total=0
    for num in number:
        total =total+num
    return total
x=my_function(20,30,40)
print(x)


def my_functuion(username, **details):
    print("username",username)
    print("Additional details:")
    for key, value in details.items():
        print(" ", key+":", value)
my_function("email23",age=23,city='oslo',hobby='coding')

def my_function(title, *args, **kwargs):
    print("Title",title)
    print("positional argument:", args)
    print("keyword argument:",kwargs)

my_function("user info", "Email", "Tobias", age=25, city="oslo")


# **********************************************
# decorator in python
"""
def changecase(func):
    def myinner():
        return func().upper
    return myinner()

@changecase
def my_funct():
    return "Hello Sally"

@changecase
def my_function():
    return "I am speed"

@changecase
def otherfunction():
    return "I am speed!"

"""

def my_function():
    return "Have a great day !"
print(myfunction._name_)

def changecase(func):
    def myinner():
        return func().upper()
    return myinner

@changecase
def addgreeting()








