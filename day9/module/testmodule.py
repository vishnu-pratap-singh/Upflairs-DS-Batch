# import module as mm
# mm.greeting("Jonathan! ")
# a= mm.person1["age"]
# print(a)
# 

import platform
x= platform.system()
print(x)


import datetime 
x=datetime.datetime.now()
print(x)

print(x.year)
print(x.strftime("%A, %B %d, %Y"))

import math
x= math.sqrt(8)
print(x)

print(math.pi)

x= ord("a")
print(x)

x= chr(97)
print(x)


import json 

x= '{"name":"John","age":30,"city":"New York"}'
#parse x
y=json.loads(x)
print(y['age'])

import re
txt ="the rain in spain"

x=re.search("^The,*spain",txt)

if x:
    print("Yes ! we have a match!")
else:
    print("No match")


txt="The rain in spain "
x=re.findall("ai",txt)
print(x)

txt ="The rain in spain"
x=re.sub("\s","0",txt)
print(x)

txt ="The rain in spain"
z=re.sub("\s","0",txt,2)
print(z)

