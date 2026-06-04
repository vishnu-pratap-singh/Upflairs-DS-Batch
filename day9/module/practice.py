# write a python using the math module to 
# find the square root of 81
# find the value of 5^3
# find the celling and flor values of 7.8

import math
x= math.sqrt(81)
print(x)
y=pow(5,3)
num=7
ceilling=math.ceil(7)
floor=math.floor(7)

"""
write a python programme using the random module to :
generate a random interger
select a random element from the list
["python","java", "C++","javscript"]





"""
import random
print(random.random())

mykist=["python","java", "C++","javscript"]
print(random.choice(mykist))





""" Exception             Description'zeroDivisionError     """
"""
wite a python program that takes teo nunbers as input from from the users and 
perform devision and handle zero devisor exception if the user enter 0 as the denominator .

"""



"""
try:
    num1=float(input('take number_1 as input '))

    num2=float(input('take num2 '))
    result = num1/num2

    print(f'result is {result}')



except zeroDivisionEroor:
    print("Error : you can not divide by zero")
except valueError:
    print("Error: Please enter valid number values")


"""



"""
write a python progrmme that accept a 
number from user
handle value error if the user enter non-numerical data
print the entered number if no exception occurs 

"""

"""
try:
    num = float(input("enter a num"))
except ValueError:
    print("Error: That is not a valid")
else:
    print(f"num is {num}")

"""


"""
wire a python programme that opens a file 
named demo.txt
write some txt into it
uses  finally black the ensures the file is closed whether an exception occurs 
or ot not 
display a message indicating that the file has been closed 


"""
try:
   file=open("demo.txt","w")
   file.write("Hello !")
   print("writing ....")

except Exception as e:
    print(f"an error occured: {e}")
finally:
    file.close()
    print("File has been closed")

