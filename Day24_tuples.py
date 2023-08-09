# Day 24

tup = (1, 2, 76, 342, 32, "green", True)
# tup[0] = 90
print('The type of tuples is:',type(tup))
print('Tuples:',tup)
print('Length of Tuples:',len(tup))
print("Tuple's element at index 0:",tup[0])
print("Tuple's element at index -1 from last:",tup[-2])
print("Tuple's element at index 2:",tup[2])
# print(tup[34])

if  3421 in tup:
  print("Yes 342 is present in this tuple")
tup2 = tup[1:4]
print(tup2)