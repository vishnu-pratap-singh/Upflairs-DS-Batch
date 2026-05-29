#string unpack
# name ="ABC"
# a,b,c=name
# print(a,b,c)

a=['divya', 'apple','juice']
x,y,z=a
print(x)
print(y)
print(z)

# concatination

x='python'
y=' is awesome'
result= x+y
print(result)

x=5
y=10
print(x+y)

x=5 
y='v'
print(x,y)
# indexing
a="hello world"
print(a[1])
print(len(a))
txt= "Best thing in life is free"
# print("free" not in txt)

if "free" in txt:
    print("Yes, 'free' is present")

# looping
# for x in 'banana':
    # print(x)



# SLICING

b= "hello, worlds!"
print(b[2:-2])
print(b[-5:-2])
print(b.upper())
print(b.lower())
a="  Hello   world   "
# print(a.strip())
#  // remove stating and ending space

print(a.replace("o", "j", 1))
ab="hello 2world"
print(ab.split("2"))

age=36
# txt ="my name is john, i am "+str(age)
txt = f"my name is john , i am {age:.2f}"
print(txt)

txt1 = "we are so called \"vikingh\" from the north"

print(txt1)


# boolean

print(10>9)
print(10==9)
print(10<9)


print(bool("abc"))
print(bool(123))
print(bool(['apple','cherry','banana']))
print(bool(""))
print(bool(()))
print(bool([]))
print(bool({}))


# &=and
# !=or
# ^=xor
# >>=left shift
# <<=right shift

# waldrus operator
print(x:=3)

x=['apple','banana']
y=['apple','banana']
z=x
print(x is z)
print(x is not y)
print(x == y)


# list 

thislist=[1, 'apple', 'banana','orange'
"cherry"]

list2 = [1,4,54,8]
list3 =[True,False, True]
print(thislist[-1])

print(thislist[2:5])
thislist[1:3]=["blackcurrent"]
print(thislist)

thislist1=['apple','banana']
thislist1.append("orange")
thislist1.insert(1,"watermealon")
print(thislist1)

tropical=['kiwi']
thislist1.extend(tropical)

thistuple=('watermealon','muskmealon')
thislist1.extend(thistuple)

print(thislist1)

# pop

fruits=['apple','banana']
fruits.pop()
print(fruits)

# clear


car=['mercedez','suzuki', 'audi']
car.clear()
print(car)

#looping

fruitname=['apple','banana', 'cherry']
for x in fruitname:
    print(x)

fruitname1=['apple','banana', 'cherry']

for i in range(len(fruitname1)):
    print(fruitname1)


# while loop
print("learning while loop \n")
mylist=['apple', 'banana', 'cherry']
i=0
while i < len(mylist):
    print(mylist[i])
    i=i+1

fruitsName= ['apple','banana', "cherry",'mango']
newlist=[]
for x in fruitsName:
    if 'a' in x:
        newlist.append(x)
    print(newlist)

# list comprehensan
fruitsName1=['apple','banana','Guava']
newlist1= [x for x in fruitsName1 if 'a' in x]
print(newlist1)

fruitsName2=['apple','banana','Guava']
newlist2= [x for x in fruitsName2 if x!= 'apple']
print('newlist2= ' ,newlist1)


numlist = [x for x in range(10)]
print(numlist)


# newlist3 = [x if x! ="banana" else "orange" for x in fruitsName2]

num=[100,50, 65, 82, 23]
num.sort(reverse=True)
print(num)

sortlist=["banana", 'Orange', 'kiwi']
sortlist.sort(key=str.lower)
print(sortlist)

thislist3= ['apple', 'banana', 'chery']
mylist4= thislist3[:]
print(thislist3)

list1 =['a','b','v','a']
print(list1.count('a'))

#apped add an element at end of list
#clear() emove all elements from list
#copy() return a copy of thre list
#count()  return the number of elements with specific value
#extend add the element of a list (or any iterable), to the end of the current list
#3INDEX() RETURN INDEX NUMBER
#insert() add element in list at particulat index(1,'a')
#pop() remkove the element at the specific position
#remove() remove the item with the specific value
# reverse reverse the order of the list
#sort() sortes the list


# create a list of 5 favourite fruits snd print:

fruits_name=['apple','banana','strawberry']
print(fruits_name)
print(fruits_name[0])
print(fruits_name[-1])




# cretate an empty list called students
# perform the following
# add a student name using append()
# print the updated list

student=[]
student.append("vishnu")
student.append("Runal")
print(student)
# 
# cretae a list of colors
# remove one color using remove
# remove last elements ucing pop
# print final list
# 

colors=['yello', 'blue', 'green']
colors.remove('blue')
colors.pop()
print(colors)

# cretate a list of numbers from 1 to 10
# print th elist
# print total numbers 

num_list = [1,2,5,7]
print(num_list)
print(len(num_list))







