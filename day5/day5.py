# # print("helo")
# # 
thisdict={
    "brand":"ford",
    "model": "Mustang",
    "Year": 1964,
    "Year":2020
 
 }

x=thisdict.keys()
print(x)
# dict_keys(['brand', 'model', 'Year'])
print(thisdict)

# {'brand': 'ford', 'model': 'Mustang', 'Year': 2020}






# updation of value with same key 

car = {
    "brand": "Ford",
    "model": "Mustang",
    "year":1965
}
print(f'car details \n {car}')
x=car.values()
print(x)

# dict_values(['Ford', 'Mustang', 1965])

car["year"]=2020
print(x)
# dict_values(['Ford', 'Mustang', 2020])

x= car.items()

print(x)
# dict_items([('brand', 'Ford'), ('model', 'Mustang'), ('year', 2020)])

car.pop("model")
print(car)

# {'brand': 'Ford', 'year': 2020}

# updating dicionary key and value

car["color"] = "white"
print(x)


# /**************Methods***************************/

# update() Method

employee={
    "Name": "vishnu",
    "ID": 112455,
    "Dept":"Data Science"
}
employee.update({"Joining":2026})
x=employee.items()
print(x)
print(employee)

# {'Name': 'vishnu', 'ID': 112455, 'Dept': 'Data Science', 'Joining': 2026}

# pop() method

x=employee.pop('Joining')
print(employee)

# {'Name': 'vishnu', 'ID': 112455, 'Dept': 'Data Science'}

# popitem() Method-  remove last inserted item

employee.update({"Joining":2026})
print(employee)

# {'Name': 'vishnu', 'ID': 112455, 'Dept': 'Data Science', 'Joining': 2026}

employee.popitem()
print(employee)

# {'Name': 'vishnu', 'ID': 112455, 'Dept': 'Data Science'}








car  ={

    "brand": "Benz",

    "model": "Mustang",

    "year":1965

}

print(car)
car.clear()
print(car) # clear all key value and print empty {}
del car
# delete entire car dictionary 
# print(car1) print  error
#
# print(car)


# ***********************looop in dictionary ***********************


products={
    "Gyser":"electronic",
    "Table" : "Furniture",
    "Shoes" : "Appearal",
    "Moile" : "electronic"

}
print(products)
# {'Gyser': 'electronic', 'Table': 'Furniture', 'Shoes': 'Appearal', 'Moile': 'electronic'}

# print throught loop
print("{")
for item, category in products.items():
    
    print(item, " : ", category)
    
print("}")

# { output
# Gyser  :  electronic
# Table  :  Furniture
# Shoes  :  Appearal
# Moile  :  electronic
# }

# print all producs whose category is electronic
item_list=[]
for item, category in products.items():
    if category == "electronic":
        item_list.append(item)
print(item_list)

# ['Gyser', 'Moile']
        



 
myfamily= {
    "child1":{
        "name":"vishnu",
        "year":2004
    },
    "child2":{
        "name":"Yogesh",
        "year":2011
    },
    "child3": {
        "name":"OM",
        "year":2011
    }
}



print(myfamily["child2"]["name"])



for x, obj in myfamily.items():
    print(x)
    for item in obj.items():
        print(item)
# 
# # clear()
# # copy()
# # fromkeys()
# # get()
# # items()
# # keys()
# # pop()
# # popitems()
# # setdefault()
# # update()
# # values()
# # 


car = {
    "brand": "Ford",
    "year": 2020
}

newcar = car.copy()
car["logo"]="generic"
print(newcar)
# {'brand': 'Ford', 'year': 2020}
print(car)  # {'brand': 'Ford', 'year': 2020, 'logo': 'generic'}

# add multiple item
car.update({
    "color": "white",
    "selfdriving": True
})
print(car)

x= car.get("model")
print(x) # None


# fromkeys() crete dictionary with keys

students = ["Rahul", "Vishnu", "Aman", "Priya"]

attendance = dict.fromkeys(students, "Absent")

print(attendance)

# create a dictionary conatining student details
# name, age, course, city

# task 
# print the complete dictionary
# print only the student name and course
# print all keys and vlues pairs

# students={
#     "Name":"Aliexa",
#     "age":22,
#     "course":"Data Science and Ai ML",
#     "city":"NW"

# }
# print(students)
# print(studnets["name"]['course'])
# for key, value in students:
#     print(f'key = {key} and values = {values}')


# # 2Q create a dictinary of 3 subject 
# add one new subject with marks
# update marks of an existing

# subjects={
#     "Operational Research":85
#     "Marketing Management":77
#     "Financial Management":82
    
# }
# subjects.add("DBMS":95)
# "Financial Management":90

# # Q3 create a dictionary of employee details
# remove one key using pop()
# remove last inserted items using subject
# print final dictionary

# employee={
#     "ID":101,
#     "name": "Runal"
#     "dept":"Finance"
#     "salry":85000
# }
# employee.pop("dept")
# print(employee)

# # Q4 take 5 favourite fruits from the user and store them in a list
# fruits =[]
# for i  in range(5):
#     fruits.append("enter a fruit name")

# # crete a frequncy dictionary
# freq_dict={}
# for fruit in fruits:
#     freq_dict[fruit]=freq_dict.get(fruit,0)+1
# print(freq)

# # Q6 favourite 5 fruit from the user and store them in a list
# # create a dict containing product name and price
# # print all product
# # print all prices
# # print product name with its price using loop 

# product={
#     "laptop":1200

# }
# print(product.keys())
# print(product.vlues())
# for name, price in product.item():
#     print(;'Product ={name}, Price ={price}')



# # Days of week

# day =input("Enter no from 1 to 7")
# if day ==1:
#     print("Sunday")
# elif day ==2:
#     print("Monday")
# elif day == 3:
#     print("Tuesday")
# elif day == 4:
#     print("Webnesday")
# elif day == 5:
#     print("Thursday")
# elif day == 6:
#     print("Friday")
# elif day == 7:
#     print("Saturday")
# else:
#     Print("Not Applicable")

# # short hand if 
# a=5:
# b=2
# if a>b: print("a is greater than b")
# # short hand if ......else
# a =2
# b=300
# print("A") if a>b else print("b")

# a=10
# b=20
# bigger=a if a>b else bprint
# print("Bigger is :", bigger)

# a = 330
# b=330
# print("A") if a>b else print("=") if a==b else print("B")

# a=200
# b=33
# c=500
#  if a>b or a>c:
#     print("At least on condition is true")


# age =25
# is_studnet=False
# has_discount=True

# if(age<18 or age>64) and not is_studnet or has_discount_code:
#     print("discount applied")


      