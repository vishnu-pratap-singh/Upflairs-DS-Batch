def student_detail(**data):
    for key,value in data.items():
        print(f" {key.capitalize()} : {value}")



    
        

student_detail(
    name='Rahul',
    age=21,
    course="python",
    city='jaipur'
)
