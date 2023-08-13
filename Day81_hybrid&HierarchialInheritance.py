# Day 81

# Example of Hybrid Inheritance 
print('This is just an example of Hybrid Inheritance')
class BaseClass:
  pass

class Derived1(BaseClass):
  pass  

class Derived2(BaseClass):
  pass  

class Derived3(Derived1, Derived2):
  pass

# Hierarchical Inheritance
print('This is just an example of Hierarchical Inheritance')
class BaseClass:
  pass

class D1(BaseClass):
  pass

class D2(BaseClass):
  pass

class D3(D1):
  pass