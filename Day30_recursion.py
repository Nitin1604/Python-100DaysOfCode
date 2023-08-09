# Day 30

# Taking the value of n from the user
n = int(input("Enter the value of n to calculate factorial: "))
def factorial(n):
  if (n == 0 or n == 1):
    return 1
  else:
    return n * factorial(n - 1)


print(factorial(n))

