# self parameter wala concept ha
class Employee:
    language = "Sanskrit" # This is a class attribute
    salary = 50000000
  
    def __init__(self, name, salary, language ): # dunder method which is automatically called
       self.name = name
       self.salary = salary
       self.language = language
       print("I am creating an object")


    def getInfo(self):
        print(f"The language is {self.language}. The salary is {self.salary}")

    @staticmethod
    def greet():
        print("Good morning")

harry = Employee("Harry", 50000, "Bengalii")
# harry.name = "Harry"
print(harry.name, harry.salary, harry.language)