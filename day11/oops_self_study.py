"""
Generality and specificity
oops has advantage you can buid your own data type 
object
Abstraction
class
polymorphisum
inheritance 

every thing is object list, tuple, ...etc are object of some class
a=2
<<type(a)>>
<class int> it means a is object of int class

to crete class it takes lots of time and space 
class is bluprint <1 data or property 
                   < 
                    functions or behaviour

car class > wheel, color .. are object of class but 
           what will be milage, Avg speed will be fuctions of class


class name should be in pascale case  ex: ThisIsPascalClass


class > Attibute >color,milage,engine
class>methods>+calAvgSpeed, +open-airbag,show_gps
+ denotes public 

L=[]
L=list()# object literals

"""

class Car:
    color="blue" #data
    model="sports" #data,
    def calculate_avg_speed(km,time):
        return km/time

print(Car.calculate_avg_speed(100,20))

