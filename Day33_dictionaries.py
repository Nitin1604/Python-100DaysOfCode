# Day 33

info = {'name':'Karan', 'age':19, 'eligible':True}
print('Getting Info:')
print('The info is:',info) 
print('')
print('Getting keys from dictinaries name info:')
print('The keys of info is:',info.keys())
print('')
print('Getting the values from dictionaries name info:')
print('The values of info is:',info.values())
print('')

for key in info.keys():
  print(f"The value corresponding to the key {key} is {info[key]}")
print('')

print('Key value pairs:',info.items())
print('')
for key, value in info.items():
  print(f"The value corresponding to the key {key} is: {value}") 
print('')

# Accessing the single values
info = {'name':'Nitin', 'age':25, 'eligible':True}
print(info['name'])
print(info.get('eligible'))  