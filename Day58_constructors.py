# Day 58

class Person:

  def __init__(self, name, occ):
    print("Hey I am a person")
    self.name = name
    self.occ = occ

  def info(self):
    print(f"{self.name} is a {self.occ}")


a = Person("Nitin", "Programmer")
b = Person("Haris Ali Khan", "best guidance to all students") 
a.info()
b.info()
print(a.name)
a.name = "Nitin"
a.occ = "Coder"
a.info()
