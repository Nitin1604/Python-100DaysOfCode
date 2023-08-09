# Day 32

# Union of two sets for numbers
setUnion1 = {1, 2, 5, 6}
setUnion2 = {3, 6, 7}
print('Union of two sets:',setUnion1.union(setUnion2))
print('Set Union 1 is:',setUnion1)
print('Set Union 2 is:',setUnion2)

# Updating the set
setUnion1.update(setUnion2)
print('Updated Set Union 1 is:',setUnion1)

# Union of two sets for strings
citiesUnion1 = {"Tokyo", "Madrid", "Berlin", "Delhi"}
citiesUnion2 = {"Tokyo", "Seoul", "Kabul", "Madrid"}
citiesUnion3 = citiesUnion1.union(citiesUnion2)
print('Union of two cities:',citiesUnion3)

# Intersection of two sets
citiesIntersection1 = {"Tokyo", "Madrid", "Berlin", "Delhi"}
citiesIntersection2 = {"Tokyo", "Seoul", "Kabul", "Madrid"}
citiesIntersection3 = citiesIntersection1.intersection(citiesIntersection2)
print('Intersection of two sets:',citiesIntersection3)

# Intersection update of two sets
citiesUpdate = {"Tokyo", "Madrid", "Berlin", "Delhi"}
citiesUpdate2 = {"Tokyo", "Seoul", "Kabul", "Madrid"}
citiesUpdate.intersection_update(citiesUpdate2)
print('Updated intersection of two sets: ',citiesUpdate)

# Symmetric Difference of two sets
cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Tokyo", "Seoul", "Kabul", "Madrid"}
cities3 = cities.symmetric_difference(cities2)
print('Symmetric Difference of two sets:',cities3)

# Symmetric Difference update of two sets
cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Tokyo", "Seoul", "Kabul", "Madrid"}
cities.symmetric_difference_update(cities2)
print('Symmetric Difference Update:',cities)

# Difference of two sets
citiesDifferent = {"Tokyo", "Madrid", "Berlin", "Delhi"}
citiesDifferent2 = {"Seoul", "Kabul", "Delhi"}
citiesDifferent3 = citiesDifferent.difference(citiesDifferent2)
print('Difference of two sets:',citiesDifferent3)

# isdisjoint() of two sets:
name = {"Nitin", "Mohit", "Bhuvnesh", "Diksha"}
# name2 = {"Saurav", "Kajol", "Mohit"}
name2 = {"Saurav", "Kajol", "Mohit"}
print('isdisjoint():',name.isdisjoint(name2))

# Another example of isdisjoint()
fruit = {"Mango", "Orange","Pineapple","Apple"}
fruit2 = {"Chiku","Gauwa"}
print('isdisjoint() example:',fruit.isdisjoint(fruit2))

# issuperset() of two sets
cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Tokyo", "Berlin"}  # checking whether whether cities2 element present in cities set or not
print('issuperset() for cities2:',cities.issuperset(cities2))
cities3 = {"Seoul", "Madrid","Kabul"}
print('issuperset() for cities3:',cities.issuperset(cities3))

# issubset() for two sets
cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Delhi", "Madrid"}
print('issubset() of cities2 from cities:',cities2.issubset(cities))

# add() of two sets
cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities.add("Hong Kong")
print('The cities added is:',cities)

# update() of two sets
cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Helsinki", "Warsaw", "Seoul"} # add these all values to sets cities
cities.update(cities2)
print('Updated cities:',cities)

# remove() of two sets
cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities.remove("Tokyo")
print('Tokyo cities removed:',cities)

'''
# remove() for not existing value in sets
cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities.remove("Seoul")
print(cities)
'''

# discard() will not raise an error
cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities.discard("Seoul")
print('Discard:',cities)

# pop() of two sets and it will remove last items
cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
item = cities.pop()
print(cities)
print(item)

# del of two sets
cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
del cities
# print(cities)  # Raise an error as set cities is entirely deleted

# clear() of two sets
cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities.clear()
print('Empty set:',cities)

# Checking if element is present or not
info = {"Nitin", 25, True, 75}
if "Nitin" in info:
    print("Nitin is present.")
else:
    print("Nitin is absent.")