class Employee:
    company = "ITC"
    def show(self):    # parent class or base class
        print(f"the name of the Employee is {self.name} and the salary is {self.salary}")

# class Programmer:
#     company = "ITC INFOSYSTEM"
#     def show(self):
#         print(f"the name of the Employee is  {self.name} and the salary is {self.salary}")

#     def show_language(self):
#         print(f"The name is {self.name} and he is good with {self.show_language} language")

class Programmer(Employee):
      company = "ITC INFOSYSTEM"   # inherit class or child class or derived class

      def show_language(self):
         print(f"The name is {self.name} and he is good with {self.show_language} language")


a = Employee()
b = Programmer()

print(a.company, b.company)
        
            