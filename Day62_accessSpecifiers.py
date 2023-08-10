# Day 62

class Student:
    def __init__(self):
        self._name = "Nitin"

    def _fullName(self):      # protected method
        return "Nitin Sokhal"

class Subject(Student):       #inherited class
    pass

obj = Student()
obj1 = Subject()
print(dir(obj))

# calling by object of Student class
print(obj._name)      
print(obj._fullName())     
# calling by object of Subject class
print(obj1._name)    
print(obj1._fullName())