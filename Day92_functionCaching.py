# Day 92

from functools import lru_cache
import time

@lru_cache(maxsize=None)
def fx(n):
  time.sleep(2)
  return n*2
    

print(fx(20))
print("done for 20") 
print(fx(2))
print("done for 2")
print(fx(6))
print("done for 6")

'''
These three print statement
(1) print("done for 20") 
(2) print("done for 2")
(3) print("done for 6")
It will compute after every 2 sec interval of time.
'''
print(fx(20))
print("done for 20") # Compute in 1 go
print(fx(2))
print("done for 2") # Compute in 1 go 
print(fx(6))
print("done for 6") # Compute in 1 go
print(fx(61))
print("done for 61") # It will compute after 2 sec but not compute in 1 go because it will not observed in python interpreter
# Output: 6765