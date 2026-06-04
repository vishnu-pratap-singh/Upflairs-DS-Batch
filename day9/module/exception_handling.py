try:
    print(x)
except NameError:
    print("variable x is not define")
except: 
    print("'An execution occurs")
finally:
    print("The 'try except'  is finished")


