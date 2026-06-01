def find_max(*numbers):

    if not numbers:
        return None

    # initializing largest num 
    largest=numbers[0]

    for num in numbers:
        if num >largest:
            largest=num

    return largest

result = find_max(10,20,40,60,11)
print(f'largest num in given  numbers = {result}')



    


