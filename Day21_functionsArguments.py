# Day 21

# Average for two numbers
def average(a, b=2):  # Default Parameters b = 2
  print("The average of two numbers is:", (a + b) / 2)

average(5)

# String Example
def name(firstName, middleName = "Pratap", lastName = "Singh"):
    print("Hello,", firstName, middleName, lastName)

name("Raja")

# Average for three numbers
print('')
def average(a, b, c=1):
   print("The average of three numbers is:", (a+b+c)/2)

average(5, 6)   

# Calculating average by using sum
def average(*numbers):
   print('The type of numbers is:',type(numbers))
   sum = 0
   for i in numbers:
      sum = sum + i
   print("Average is:", sum / len(numbers))

average(5, 6)

# Keyword Arbitrary Arguments:
def name(**name):
    print('The type of name is:',type(name))
    print("Bolo,", name["firstName"], name["middleName"], name["lastName"])

name(middleName = "Siya", lastName= "Ram", firstName = "Ram")