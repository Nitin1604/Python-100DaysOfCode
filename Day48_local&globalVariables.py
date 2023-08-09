# Day 48

x = 10  # global variable


def my_function():
  global x
  x = 5  # this will change the value of the global variable x
  y = 5  # local variable


my_function()
print('x is: ',x)  # prints 5
# print(y) # this will cause an error because y is a local variable and is not accessible outside of the function

print('')
print('Another example of local and global variables')

x = 2
print('x is: ',x)

def greeting():
  x = 6
  print(f"The local x is: {x}")
  print("Hi Nitin")

print(f'The global x is: {x}')
greeting()
x = 6
print(f'The global x is: {x}')
