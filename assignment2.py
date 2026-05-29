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
