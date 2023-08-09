# Day 53

# MAP 
def cube(x):
  return x * x * x


print('Cube of 2 is:',cube(2))

l = [1, 2, 4, 6, 4, 3]
newl = []
for item in l:
  newl.append(cube(item))

newList1 = list(map(lambda x: x*x*x, l))
print('newList1:',newList1)

# FILTER
def filter_function(a):
  return a>2
  
newList2 = list(filter(filter_function, l))
print('newList2:',newList2)

from functools import reduce

# List of numbers
numbers = [1, 2, 3, 4, 5] 

# Calculate the sum of the numbers using the reduce function
def mysum(x, y):
  return x + y
  
sum = reduce(mysum, numbers)

# Print the sum
print('sum:',sum)