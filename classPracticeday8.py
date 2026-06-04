print("hello")
"""
write a decorator that prints:
function started
before executing a function and function ended
after the function executing 
apply it to a function that prints "hello python"
"""


print("----Question 1------")
def mydecorator(func):

    def innerfunc():

        print("Before function")

        func()

        print("after functin")

    return innerfunc



@mydecorator

def say_hello():

    print("Hello world")

say_hello()





""" 
cretae a decorator that display a message before and after function runs 
apply it toa function that calculate the sum of numbers from 1 to 100
print function started before executing a function and 
print function ended after the function execution

"""


print("---Question 2-------")


def sum_decorator(func):
    def innersumfunc():
        print("function started")
        func()
        print("function ended")
    return innersumfunc
@sum_decorator
def calculate_sum():
    total = sum(range(1,100))
    print(f'the sum from 1 to 100 is {total}')
calculate_sum()
    

"""
write a function *args that accept any number of argument and retuns thair sum
example  sum_num(10,20m30,40)
output 40
"""


print("---Question 3-------")
def total_sum(*args):
    return sum(args)
sum_num=total_sum(10,20,30,40)
print(sum_num)


"""
write a function using **kwargs that accept employee details such as :
Name 
department
salary
experience
print all setails in a formatted manner;

"""
def employee_detail(**kwargs):
    print("--Employee Details----")
    for key, value in kwargs.items():
        print(f'{key} : {value}')
    

employee_detail(
    name="Alia",
    department='engineering',
    salary=854255,
    experience='5 years'
)


