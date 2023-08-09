# Day 25

# Tuples are immutable means that they are not changed once they are defined...
tuples = (0, 1, 2, 3, 2, 31, 1, 3, 2, 3)
res = tuples.count(3)
res = tuples.index(3)
# res = tuples.index(311)  # Throw an error because 311 is not present in tuples...
res = tuples.index(3, 4, 8)
res = len(tuples)
print('Count of 3 in tuples is:', res)