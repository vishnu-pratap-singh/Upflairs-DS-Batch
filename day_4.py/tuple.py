# thistuple=('apple',)
# print(type(thistuple))
# 
# y=list(thistuple)
# y.append('orange')
# 
# print(thistuple)


fruits =('apple', 'banana', 'cherry','strawbwrry')
(green, *yello, red)=fruits
print(green)
print(yello)
print(red)


fruit =('apple', 'banana', 'cherry')
mytuple=fruit*2
print(mytuple)

# sets 
# orderd immutable not allow duplictae
print('now sets \n')
thisset = {'apple','banana', 'apple'}
print(thisset)

this_set ={'apple','banana', 0, False,1,2}
print(this_set)

# addition in set 
tropical=['kiwi']
thisset.add("orange")
print(thisset)
# add list in set
thisset.update(tropical)
print(thisset)


thisset.remove("banana")
print(thisset)

# out put {'orange', 'kiwi', 'apple'}


x= thisset.pop()
print(x)
print(thisset)

# set1={'a','b','c'}
# set2={'1','2','3'}
# set3=set1 | set2
# print("set 3 is ", set3)
# set 3 is  {'2', '1', 'c', 'b', 'a', '3'}
# 

# set1 ={'apple', 'banana', 'cherry'}
# set2 ={'google', 'microsoft', 'apple'}
# print(set1.intersection(set2))

# 
# set1 ={'apple', 'banana', 'chery'}
# set2 ={'google', 'microsoft', 'apple'}
# set1.intersection_update(set2)
# print(set1)
# {'apple'}

# difference 
set1 ={'apple', 'banana', 'chery'}
set2 ={'google', 'microsoft', 'apple'}
set1.difference(set2)
print(set1)





set1 ={'apple', 'banana', 'chery'}
set2 ={'google', 'microsoft', 'apple'}
set1.difference_update(set2)



set1 ={'apple', 'banana', 'chery'}
set2 ={'google', 'microsoft', 'apple'}
set3= set1.symmetric_difference(set2)


# x= frozenset{{'apple','banana','cherry'}}
# print(x.remove('banana'))




