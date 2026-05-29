# write a python programme to print name course age and city
 
# name="vishnu"
# course="Data Science with Ai and ML"
# age=26
# print(f"my name is {name} and course {course} , i am {age} year old")

# Q2. Take user input for name and age then print Hello <name> your age > year old
# 
# my_name = input('Enter your name')
# 
# my_age  = input('Enter your age')
# 
# print('my name is ', my_name, 'and i am ',my_age, ' yaer old')

# Q3
# writa a [rogramme to ]
#  take a string input
#  print its reverse
#  count total number of character


# string_example= input('Enter any string for example')
# print(len(string_example))
# reverse_string = string_example[::-1]
# print(reverse_string)


# Q4. crete a set containing duplicate numbers
#  print the original set
#  observe how duplicate are automatically removed 
#  add a new element using add()
#  remove an element using remove()
# 
# car = {'creta', 4, 'ertiga',7, 'scorpio',
# 4,}
# 
# print(car)
# 
# car.add('benz')
# print(car)
# 
# remove_one= car.remove('benz')
# print(car)


# Q5 create a tuple of 6 number
#   print the maximum and minimum number
#   count how many times a specific number appear
#   find the index position of given element

tuple1= (4,70,5,45,23,48)


heighest=tuple1[0]
lowest= tuple1[0]

for num in tuple1[1:]:
    if num >heighest:
        heighest=num
    

    if num < lowest:
        lowest=num

print(f'max value is {heighest}')
print(f'min value is {lowest}')


# tuple2 = (4,70,5,45, 5,23,48)
# target=5
# count=0
# curr_index=0
# get_index=[]
# for num in tuple2:
    # if num == tyaget:
        # count=count+1
        # get_index.append(curr_index)
# 
    # curr_index=curr_index+1
# print(f'count of 5 occurance is {count}')





