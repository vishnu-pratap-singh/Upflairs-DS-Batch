def calculate_salary(basic, bonus =2000, tax=10):
    gross_salry=basic+bonus
    # deduct tax percentage
    net_salary = gross_salry-(gross_salry*(tax/100))
    return net_salary

    # calling the function using only basic 
salary_default=calculate_salary(50000)
print(salary_default)

    # b) calling function by providing all argument 

custom_salary= calculate_salary(50000,5000,15)
print(f'net salay custom value {custom_salary}')

