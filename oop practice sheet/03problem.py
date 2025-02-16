class Demo:
    a = 4

o = Demo()
print(o.a) # pRINTS THE CLASS ATTRIBUTE BECAUSE INSTANCE ATTRIBUTE IS NOT PRESENT

o.a = 0    # instance attribute is present
print(o.a) # Prints the instance attributes  because instance 
# attribute is present
print(Demo.a) # Print the class attributes

# no class attribute is not change


