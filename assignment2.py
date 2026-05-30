print("Hello Welcome to second assignment")

# ***********Assignment 2***********

# q1 write a python programme for Atm withdrawl using IF_Else
# condition:
#   user should enter correct PIN 
#   Balnce should be greater than withdrawal amount
#   withdrawal amount should be multiple of 100




balance= int(input("Enter your account balance "))
pin = int(input("Enter Atm 6 digit pin "))
Amount_withdraw=int(input("Enter Amount you want to withdraw "))

if balance<Amount_withdraw:
    print("Insufficient Balace ")
if len(str(pin))!=6:
    print("Invalid PIN")
if Amount_withdraw % 100 ==0:
    print(f"Successful withdrawal and remaining amount  {balance-Amount_withdraw}")
else:
    print("Invalid Amount")

# 
# **********output*********************
# Hello Welcome to second assignment
# Enter your account balance 50000
# Enter Atm 6 digit pin 123456
# Enter Amount you want to withdraw 20000
# Successful withdrawal and remaining amount 30000
# ***********************************************


# *****************question 2*************************


#write a pyhton programme using i else to: 
# check whether a year is leap year or not 
# display number of days in given month 
# feb has 29 days in leap year  otherwise 28
# task take year and month as input 
#print total days in that month

# **********************code **********************


months_dict = {
   "january" : 31,
   "February" :28,
   "march" :   31,
   "april" :   30,
   "may"   :   31,
   "june"  :   30,
   "july"  :   31,
   "August" :  31,
   "september": 30,
   "october" : 31,
   "november" : 30,
   "december" : 31
}


year = int(input("Enter year... "))
month=input("Enter month name january, february ... ").lower()

if month not in months_dict:
    print("Invalid month")


if (year % 4==0 and year % 100 != 0) or year % 400==0:
    if month == "february":
        months_dict[month]=29

    print(f'{year} is a leap year and given {month} has {months_dict[month]} days')

    
else:
    print(f'{year} is not a leap year given {month} has {months_dict[month]} days')



# ***************************end *********************




# *********************question 3********************


# write a python programme A) take two number input
# perform Addition, substractio, multiplication, division, modulus


a=int(input("Enter any number"))
b=int(input("Enter second number"))
print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a%b)




# ******************Question 4 **********************************************************

# write  python progamme to create a list of square of numbers from 1 to 20 using list comprehension
# also create anoter list containing only even squares


square=[num*num for num in range(1,20)]

print(square)

even_square=[num*num for num in range(1,20) if num%2==0]
print(even_square)




# ***************************question 5 *************************************************

"""
create a dictionary name 5 students and their marks 
task print marks od a particular student
find the student with highest marks
add one new studnet with marks 
"""

students={
    "vishnu" : 92,
    "Akil"   :85,
    "chandan":86

}
print(students["vishnu"])
top_student=None
highest_marks=-1
for student, marks in students.items():
    if marks > highest_marks:
        highest_marks=marks
        top_student=student

print(f"student with highest marks {top_student} @ score {highest_marks}")

# """ output :
            #  student with highest marks vishnu @ score 92
# 
# """
# 

"""
create a dic store student details(name, age ,course) create a set of 5 unique num
take a num as string and convert it into integer using type casting
print all values properly

"""

student_detail={
    "name":"shallu",
    "age" : 25,
    "course": "MBA"

}
print(student_detail)

unique_num={10,25,30,45}

num=string(input("enter num"))
num_integer=int(num)
print("\n type casting result ")
print(f'original string {num} and type casted value {num_integer}')

















