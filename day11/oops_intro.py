print("hello class and object")
"""
class MyClass:
    x=3

"""
# pl=MyClass()
# print(pl.x)
# del pl
# print(pl.x) this will raise error bcoz pl is deleted

"""
p1=MyClass()
p2=MyClass()
p3=MyClass()

print(p1.x)
print(p2.x)
print(p3.x)
"""

# 
# 
# class Person:


    # pass
# 


class Person:
    def _init_(self,name, age=18,country="US",city="Delhi"):
        self.name=name 
        self.age=age 
        self.country=country
        self.city=city

p1=Person("nikhil",20,"india","mumbai")
# p2=Person("OM")
print(p1.name)
print(p1.age)
print(p1.country)
print(p1.city)


