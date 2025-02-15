class Employee:
    language = "Sanskrit" # This is a class attribute
    salary = 50000000

Om = Employee()
Om.name = "OM Tripathi" # This is an object/instance attribute
print(Om.name, Om.language, Om.salary)

Rohan = Employee()
Rohan.name = "Rohan Rudra Mahadev"
print(Rohan.name, Rohan.language, Rohan.salary)


# here name is object/instance attribute 
# and salary and language are 
# class attributes as they directly belong to 
# the class