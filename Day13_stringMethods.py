""" Day 13 """
# Strings are immutable
a = "Nitin Sokhal ..."

# Checking the length of the string
print('The length of a is:',len(a))

# Printing the value of a
print('The value of a is:',a)

# Converting the given  text into Uppercase format
print('The Uppercase is:',a.upper())

# Converting the given  text into Lowercase format
print('THe lowercase is:',a.lower())

# Removing the extra special symbol by rstrip method.
print('The rstrip is:',a.rstrip("..."))

# Replace the given word to another new word
print('Replace value is:',a.replace("Nitin", "John"))

# Split the given word with some space or some another character
print('Splitting is:',a.split(" "))
blogHeading = "introduction tO jS"

# Capitalize the first word of the sentence and make the rest in lowercase format
print('The blogHeading is:',blogHeading.capitalize())

str1 = "Welcome to the Python Interpreter!!!"

# Checking the length of the string
print('The length of str1 is:',len(str1))

# Center the given string with length method
print('The length of str1 center is:',len(str1.center(5)))

# Center the given string with some space number given
print('The str1 of center is:',str1.center(50))

# Count the given alphabets of a given string
print('Count of given alphabets:',a.count("Nitin"))

str1 = "Welcome to the Python Interpreter !!!"

# Checking the given string whether its ends with some special characters or not.
print('Value endswith:',str1.endswith("!!!"))

# You can also override the value of str1
str1 = "Welcome to the Python Interpreter !!!"

# Checking the given string ends with "to" or not from given starting index and ending index.
print('Value endswith this:',str1.endswith("to", 4, 10))

str1 = "He's name is Dan. He is an honest man."

# Checking the particular words in the given string.
print('Finding words:',str1.find("ishh"))
# print(str1.index("ishh"))

str1 = "WelcomeToThePythonInterpreter"

# Checking the string whether it contains A-Z, a-z, 0-9 and if some other characters return false
print('isalnum:',str1.isalnum())
str1 = "Welcome"

# Checking the given string should contains A-Z, a-z but it shouldn't contain any numbers (0-9)
print('isalpha:',str1.isalpha())

str1 = "hello world"

# Converting the given string to lowercase format.
print('islower:',str1.islower())

str1 = "We wish you a Merry Christmas\n"

# All characters in the given string will be in printable form but it shouldn't contain any other characters "\n" , "\t"
print('isprintable:',str1.isprintable())

str1 = "         "       #using Spacebar

# Checking the space in the given string
print('isspace:',str1.isspace())

str2 = "  "       #using Tab

# Checking the space in the given string
print('isspace value:',str2.isspace())

str1 = "World Health Organization" 

# Checking every first word of the given string is it in Captial format or not
print('istitle str1:',str1.istitle())

str2 = "To kill a Mocking bird"

# Checking every first word of the given string is it in Captial format or not
print('istitle str2:',str2.istitle())

# Checking the given string starts with particular word or not
str1 = "Python is a Interpreted Language" 
print('str1 startswith:',str1.startswith("Python"))

# swapcase will convert the lowercase to uppercase and uppercase to lowercase
str1 = "Python is a Interpreted Language" 
print('str1 swapcase:',str1.swapcase())

str1 = "His name is Dan. Dan is an honest man."

# Checking every first character are in Uppercase or not.
print('str1 title:',str1.title())