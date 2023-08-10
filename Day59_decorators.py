# Day 59

# Decorators
def greet(function):
  def modifiedFunc(*args, **kwargs):
    print("Good Morning")
    function(*args, **kwargs)
    print("Function body")
  return modifiedFunc

@greet
def hello():
  print("Inside decorator written with @greet")

@greet
def add(a, b):
  print(a+b)
  
greet(hello)()
hello()
greet(add)(1, 2)
add(1, 2)