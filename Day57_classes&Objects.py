# Day 57

class Person:
  name = "Nitin"
  occupation = "Software Developer"
  networth = 100000
  def info(self):
    print(f"{self.name} is a {self.occupation}")

# self ka mtlb: Wo object jis pr ye method call ho rha hai jaise ki a.info() , b.info() , c.info()
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