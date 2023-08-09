# Day 19
print('Continue Statement')
for i in range(12):
  if(i == 10):
    print("Iteration is skipped for i = 10")
    continue   # Iteration done from i = 0 and i = 9 but skip iteration for i = 10 and continue iteration for i = 11
  print("5 X", i, "=", 5 * i)

print('')  
print('Break Statement')  
i = 0
while True:
  print(i)
  i = i + 1
  if(i%10 == 0):
    break

print("It will terminate the loop when it meet iteration at 10..this is break statement")