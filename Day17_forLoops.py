# Day 17
name = 'Nitin'
print('For Loops Example:')
for i in name:
  print(i)
  if(i =="i"):
    print("Letter print hone shuru hue hai")
    
print('')    
print('List Example:')    
colors = ["Red", "Green", "Blue", "Yellow"]
for color in colors:
  print(color)
  for char in color:
    print(char)

print('')
name = ['Nitin','Himanshu','Himanshi','Deepanshu','Deepanshi','Jatin','Yatin']
for names in name:
  print(names)
  for j in names:
    print(j)

print('')
print('Range Function Example 1:')
for k in range(5):
  print(k + 1)
  
print('')
print('Range Function Example 2:')
for k in range(1, 6):
  print(k)
  
print('')
print('Range Function Example 3:')
# for iterator in range(start , stop, step)
for k in range(1, 12, 3):  # start = 1 , stop = 12 , step = 3
  print(k)