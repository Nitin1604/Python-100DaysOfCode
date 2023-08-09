# Day 52

def double(x):
  return x*2

def appl(fx, value):
  return 6 + fx(value)

double = lambda x: x * 2
cube = lambda x: x * x * x
avg = lambda x, y, z: (x + y + z) / 3

print('Double of 5 is:',double(5))
print('Cube of 5 is:',cube(5))
print('Average of three numbers:',avg(3, 5, 10))
print('Lmabda Functions:',appl(lambda x: x * x , 2))