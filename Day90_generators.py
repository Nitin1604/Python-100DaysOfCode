# Day 90

def my_generator():
    for i in range(6):
      # Complex computations
      yield i

gen = my_generator()
# 1st Method of generator

'''
print('1st gen: ',next(gen))
print('2nd gen: ',next(gen))
print('3rd gen: ',next(gen))
print('4th gen: ',next(gen))
print('5th gen: ',next(gen))
print('6th gen: ',next(gen))
'''

# 2nd Method of generator
for j in  gen:
  print('gen: ',j)

# Another example of generator
def new_generator():
   for k in range(7):
      yield k

gen1 = new_generator()      
for n in  gen1:
  print('gen1: ',n)
