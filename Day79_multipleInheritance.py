# Day 79

class Employee:
  def __init__(self, name):
    self.name = name
  def show(self):
    print(f"The name is {self.name}")

class Dancer:
  def __init__(self, dance):
    self.dance = dance

  def show(self):
    print(f"The dance is {self.dance}")

class DancerEmployee(Employee, Dancer):
  def __init__(self, dance, name):
    self.dance = dance
    self.name = name

dancerEmp  = DancerEmployee("Kathak", "Shivani")
print(dancerEmp.name)
print(dancerEmp.dance)
dancerEmp.show() 
print(DancerEmployee.mro())