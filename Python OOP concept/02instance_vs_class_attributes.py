class Employee:
    language = "Sanskrit" # This is a class attribute
    salary = 50000000

Om = Employee()
Om.language = "Tamil ella" # This is an object/instance attribute
print( Om.language, Om.salary)

# note: instance attributes is more preferable in 
# class attributes