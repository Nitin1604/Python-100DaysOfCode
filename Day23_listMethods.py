# Day 23

# Appending the list
print('-------List Method-------')
list = [1, 2, 4, 6]
print('Before appending 21:',list)
list.append(21)
print('')
print('After appending 21:',list)
print('')

# Sorting the list
sortList = [95, 1 , 45, 15, 12, 100]
sortList.sort()
print('Sorted List:',sortList)
print('')

# Reversing the string
reversedList = [1, 2, 3, 4, 5, 6]
reversedList.reverse()
print('Reversing the list:',reversedList)
print('')

# Index for any array elements
list = [1, 2, 4, 6]
print('List:',list)
print('The element 1 is present at index:',list.index(1))
print('')
print('The element 2 is present at index:',list.index(2))
print('')
print('The element 4 is present at index:',list.index(4))
print('')
print('The element 6 is present at index:',list.index(6))

# Count Method
countList = [1,2,3,4,5,6,7,1,2,4,1]
print('')
print('Count is:',countList.count(4))
print('')

# Copy method
listCopy = [11, 45, 1, 2, 4, 6, 1, 1]
newList = listCopy.copy()
print('Copy List:',newList)
print('')

# Insert method
listInsert = [12, 46, 2, 3, 5, 7, 2, 3]
listInsert.insert(1,48)
print('Inserted List:',listInsert)
print('')

# Extend method
listExtend = [22, 550, 456]
listInsert.extend(listExtend)
print('Extending List:',listInsert)
print('')

# Concatenation of two list
listA = [1, 2, 4, 6]
listB = [6, 4, 2, 1]
listConcat = listA + listB
print('Concat list:',listConcat)