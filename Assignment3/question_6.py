numbers=[5,12,17,18,24,32]
even_numbers=list(filter(lambda x:x%2 ==0, numbers))

squares=list(map(lambda x:x**2, even_numbers))

print("Even Numbers :", even_numbers)
print("Squares :", squares)