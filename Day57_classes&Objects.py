# Day 57

class Person:
  name = "Nitin"
  occupation = "Software Developer"
  networth = 10
  def info(self):
    print(f"{self.name} is a {self.occupation}")


a = Person()
b = Person()
c = Person()

a.name = "Shubham"
a.occupation = "Accountant"

b.name = "Nitika"
b.occupation = "HR"

print('The [a.name] is: ',a.name)
print('The [a.occupation] is: ',a.occupation)
a.info()
b.info()
c.info()