# Day 28

# Example 1:
letter = "Hey my name is {1} and I am from {0}"   # "Hey my name is {1} and I am from {0} | name (1) => Nitin || country (0) => India |"
country = "India"
name = "Nitin"

# Example 2:
foodLike = "I like {} juice and {} vegetables"   # "I like {juice} juice and {vegetables} vegetables | juice => Mango || vegetables => Capsicum
juice = "Mango"
vegetables = "Capsicum"
print(foodLike.format(juice, vegetables))


print(letter.format(country, name))
print(f"Hey my name is {name} and I am from {country}")
print('')
print('1st way to show f-string:')
print(f"We use f-strings like this: Hey my name is {{name}} and I am from {{country}}")
print('')
print('2nd way to show f-string:')
print("We use f-strings like this: Hey my name is {name} and I am from {country}")
print('')
price = 49.09999
txt = f"For only {price:.2f} dollars!"
print(txt)
# print(txt.format())
print(type(f"{2 * 30}"))