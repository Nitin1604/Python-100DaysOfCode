# Day 63

# Import random module here
import random

userInput = input("Enter your choice : ")

# randomChoices from snake, water and gun
randomChoices =[ "snake" , "water" , "gun"]

# using random module here
cpuInput =random.choice(randomChoices)

# printing cpuInput whether cpu choose
print(cpuInput)

# userInput : snake  and cpuInput : water
if userInput == "snake" and cpuInput =="water":
  print("userInput wins")

# userInput : water  and cpuInput : snake
if userInput == "water" and cpuInput== "snake":
  print("cpuInput wins")

# userInput : gun  and cpuInput : snake
if userInput == "gun" and cpuInput =="snake":
  print("userInput wins")

# userInput : snake  and cpuInput : gun
if userInput == "snake" and cpuInput== "gun":
  print("cpuInput wins")

# userInput : water  and cpuInput : gun
if userInput == "water" and cpuInput =="gun":
  print("userInput wins")

# userInput : gun  and cpuInput : water
if userInput == "gun" and cpuInput== "water":
  print("cpuInput wins")

# When both player have same choices i.e snake , snake | gun , gun | water , water 
if userInput==cpuInput or cpuInput==userInput:
  print("Draw")