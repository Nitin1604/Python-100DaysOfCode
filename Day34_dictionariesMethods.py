# Day 34

dictMethod1 = {122: 45, 123: 89, 567: 69, 670: 69}
dictMethod2 = {222: 67, 566: 90}

dictMethod1.update(dictMethod2)
# dictMethod1.clear()
# dictMethod1.pop(122)
dictMethod1.popitem()
del dictMethod1[122]
print(dictMethod1) 