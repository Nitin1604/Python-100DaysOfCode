# Day 61

class Employee:
  def __init__(self, name, id):
    self.name = name
    self.id = id 

  def showDetails(self):
    print(f"The name of Employee: {self.id} is {self.name}")

class Programmer(Employee):
  def showLanguage(self):
    print("The default langauge is Python")


employee1 = Employee("Niharika", 400)
employee1.showDetails()
employee2 = Programmer("Nitin", 4100)
employee2.showDetails()
employee2.showLanguage()