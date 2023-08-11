# Day 65

class Math:
  def __init__(self, num):
    self.num = num

  def addtonum(self, n):
    self.num = self.num +n
    
  @staticmethod
  def add(a, b):
      return a + b

result = Math.add(1, 2)
print('Result: ',result) # Output: 3
a = Math(5)
print('a.num for Math(5): ',a.num)
a.addtonum(6)
print('a.num for addtonum(6): ',a.num)

print('Math.add(7,2): ',Math.add(7, 2)) 