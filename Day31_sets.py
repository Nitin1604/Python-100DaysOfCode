# Day 31

# Set can only accept distinct values but it will not accept duplicate values in a set and they can't be change once they are created.
pythonSet = {2, 4, 2, 6}
print('The set is:',pythonSet)
print('')

setInfo = {"Jawa 42 Bike", 19, False, 5.9, 19}
print('Information of set is:',setInfo)
print('')

nitin = set()
print('The type of set is:',type(nitin))
print('')

for value in setInfo:
  print('Value:',value)
print('')

emptyDict = {}
print('The type of this emptyDict is:',type(emptyDict))
print('')

emptySet = set()
print('The type of this emptySet is:',type(emptySet))
print('')

# create a set of integer type
student_id = {112, 114, 116, 118, 115}
print('Student ID:', student_id)
print('')

# create a set of string type
vowel_letters = {'a', 'e', 'i', 'o', 'u'}
print('Vowel Letters:', vowel_letters)
print('')

# create a set of mixed data types
mixed_set = {'Hello', 101, -2, 'Bye'}
print('Set of mixed data types:', mixed_set)