# Day 22

marks = [3, 5, 6, "Nitin", True, 6, 7 , 2, 32, 345, 23]
# index: 0  1  2     3       4   5  6   7  8    9   10
print('The marks are:',marks)
print('The type of marks is:',type(marks))
print(marks[0], marks[1], marks[2], marks[3], marks[4], marks[5])

print('The negative index is:',marks[-3]) # Negative index
print('The positive index is:',marks[len(marks)-3]) # Positive index
print('The positive index of marks at index 2 is:',marks[2]) # Positive index
print('THe positive index of marks at index 8 is:',marks[8]) # Positive index
print('The positive index of mark at index 2 is:',marks[2]) # Positive index

if "6" in marks:
  print("Yes")
else:
  print("No")

# Same thing applies for strings as well!
print('')
print("Examples for string:")
if "Ni" in "Nitin":
  print("Yes")

print('')
print('List starting and ending index:')
print('Starting index 0 & ending index 7:',marks[0:7])
print('Starting index 1 and ending 9:',marks[1:9])
print('Jump index slicing index 1 to index 9 and jump index of 3:',marks[1:9:3])

lst = [i*i for i in range(10)]
print(lst)
lst = [i*i for i in range(10) if i%2==0]
print(lst)