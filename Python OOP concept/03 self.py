# self parameter wala concept ha
class Employee:
    language = "Sanskrit" # This is a class attribute
    salary = 50000000
  
    def getInfo(self):
        print(f"The language is {self.language}. The salary is {self.salary}")

    @staticmethod
    def greet():
        print("Good morning")

harry = Employee()
# harry.language = "TAMIL ELLA " "THIS IS AN INSTANCE ATTRIBUTE"
harry.greet()
harry.getInfo()
# Employee.getInfo(harry)