# Day 39

questions = [
  [
    " Q1 : Which language was used to create fb?", "Python", "French", "JavaScript",
    "Php", 4
  ],
  [
    " Q2 : Which language was used to create animation?", "HTML", "CSS", "JavaScript",
    "C++", 2
  ],
  [
    "Q3 : Who developed the language Python?", "Guido van Rossum", "Albert Einstein", "Thomas Alva Edison",
    "None", 1
  ],
  [
    " Q4: Who developed react js?", "Jordan Singh", "Jordan Walke", "Guido Van Rossum",
    "None",  2
  ],
  [
    "Q5:Who developed C++ ", "Dennis Ritchie", "Brian Kernighan", "Rob Pike",
    "Jordan Walke",  1
  ],
  [
    "Q6 : Who developed C?", "Dennis Ritchie", "Rob Pike", "Brian Kernighan",
    "PK",  1
  ],
  [
    "Q7 : Who developed HTML?", "Tim Berners-Lee", "Krisno Ronaldo", "Kris Gyel",
    "Rob Pike",  1
  ],
  [
    "Q8 : Who developed CSS?", "Håkon Wium Pie", "Elon Musk", "Jonas David",
    "Håkon Wium Lie",  4
  ],
  [
    "Q9 : Who developed JavaScript?", "Brendan Kumar", "Brendan Eich", "Imran Khan",
    "Salman Khan",  2
  ],
  [
    "Q10 : Who developed Php?", "Amir Khan", "Jeo Biden", "Rasmus Lerdorf",
    "None of these",  3
  ],
  [
    "Q11 : What is full form of CSS?", "Cascading Style Separate", "Cascading Style Sheets", "Corner Style Sheets",
    "None of these",  2
  ],
  [
    "Q12 : What is full form of HTML?", "Hightext Mark it Language", "Hypertext Markup Language", "Highertext Mark in language",
    "None",  2
  ],
  [
    "Q13 : What is the syntax for declaring function in python?", "def", "function()", "def()",
    "Function syntax is not available in python",  1
  ],
  [
    "Q14 : How many types of functions in javascript?", "One ", "Two", "Three",
    "Four",  2
  ],
  [
    "Q15 : Which language was used to create web page alive?", "Python", "C++", "JavaScript",
    "Php",  3
  ],
 
  [
    "Q16 : Which language is easy to learn and have indentation when not giving identation in code?", "Python", "C++", "JavaScript",
    "C",  1
  ],
  
  [
    "Q17: How useState hook written in React JS?",  'import { useState } from "react"', 'import { stateUse } from "react";', 'useState hook is not available in react js', 'None of the above'
  ]
]

levels = [1000, 2000, 3000, 5000, 10000, 20000, 40000, 80000, 160000, 320000,640000, 1250000, 2500000, 5000000, 7500000, 10000000, 75000000]
money = 0
for i in range(0, len(questions)):
  
  question = questions[i]
  print(f"\n\nQuestion for Rs. {levels[i]}")
  print(f"a. {question[1]}          b. {question[2]} ")
  print(f"c. {question[3]}          d. {question[4]} ")
  reply = int(input("Enter your answer (1-4) or  0 to quit:" ))
  if (reply == 0):
    money = levels[i-1]
    break
  if(reply == question[-1]):
    print(f"Correct answer, you have won Rs. {levels[i]}")
    if(i == 4):
      money = 10000
    elif(i == 9):
      money = 320000
    elif(i == 14):
      money = 7500000
      print('You have passed the level Dhan Amrit Padhav of ₹7500000')
    elif(i==15):
      money = 10000000
      print('Congrulations You have won ₹1 crore')
    elif(i == 16):
      money = 75000000
      print('Congrulations You have won ₹7.5 crore')
  else:
    print("Wrong answer!")
    break 

print(f"Your take money to home is Rs {money}")