# Day 72

class Employee:
  def __init__(self, name, id):
    self.name = name
    self.id = id

class Programmer(Employee):
  def __init__(self, name, id, lang):
    super().__init__( name, id)
    self.lang = lang

Sonalika = Employee("Sonalika", "400")
Nitin = Programmer("Nitin", "645", "Python")
print(Nitin.name)
print(Nitin.id)
print(Nitin.lang)