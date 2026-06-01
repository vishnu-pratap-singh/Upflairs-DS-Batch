# i =1
# while i <6:
    # print(i)
    # if i==3:
        # continue
    # i+=1
# print("i")
# 
i=0
while i<6:
    i+=1
    if i== 3:
        continue
    print(i)


# i=1
# while i<6:
    # print(i)
    # i+=1
# else:
    # print('i is no loger 6')


fruits =['apple', 'banana', 'cherry']
for x in fruits:
    if x == "banana":
        continue
    print(x)

print('\n')
adj =['read', 'big', 'tasty']
fruits=['apple', 'banana', 'cherry']
for x in adj:
    for y in fruits:
        print(x,y)

print("function \n")

def farenheit_to_celsius(farenhite):
    return (farenhite-32)*5/9

print(farenheit_to_celsius(77))


def get_greeting():
    return "Hello from a function"
message=get_greeting()
print(message)

def my_function(fname):
    print(fname+ "student")

my_function("Alica")
my_function("Silva")

def myfun(fname, lname):
    print(fname +" "+lname)
myfun("vishnu", "singh")

def myfunction(name="friend"):
    print("hello", name)
myfunction("A")

# def my_funct(animal,name):
    # print("i have a", animal)
# 
# myfunct("Buddy", "dog")
# 


def myfunction2(person):
    print("name", person["name"])
    print("Age", person["age"])

person={"name":"gargi","age":20}
myfunction2(person)




def myfunction3():
    return(10,20)
x,y =myfunction3()
print("x :",x) 
print("y: ",y)


def my_function4(name, /):
    print("Hello",name)

my_function4("Email")


# def my_function5(name, /):
# 
    # print("Hello",name)
# 
# my_function4(name="emil")
# 
r=range(10)
print(r[2])
print(r[:3])

r=range(0,10,12)
print(6 in r)
print(7 in r)

r=range(0,10,2)
print(len(r))


#
# write a python programme to find sum of all number from 1 to N using rannge() function 

def sumofnum(N):
    totalsum = sum(range(1,N+1))
    return totalsum
x=sumofnum(10)
print(x)


# cretae a list of num[12345678910]
# count total even number 
# display total odd numbers
# display both count
# 

list_num=[1,2,3,4,5,6,7,8,9,10]

def countEven():
    
    evencount=0
    for num in list_num:
        if num % 2 == 0:
            evencount=evencount+1
           
    return evencount

  
print(countEven())


def countOdd():
    oddCount=0
    for num in countOdd:
        if num %2 !=0:
            oddCount+=1
        
    return oddCount

print(countOdd())






