class Employee:
    company = "ITC"
    name = "Defailt name"
    def show(self):    # parent class or base class
        print(f"the name of the Employee is {self.name} and the company  is {self.company}")

class Coder:
    language = "Python"
    def printLanguages(self):
        print(f"Out of all the languages here is your language: {self.language}")

class Programmer(Employee, Coder):
      company = "ITC INFOSYSTEM"   # inherit class or child class or derived class
      def showLanguage(self):
         print(f"The name is {self.company} and he is good with {self.language} language")


a = Employee()
b = Programmer()

b.show()
b.printLanguages()
b.showLanguage()

        
            