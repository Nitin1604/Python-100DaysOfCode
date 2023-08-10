# Day 63

import random

userInput = input("Enter your choice : ")

randomChoices =[ "snake" , "water" , "gun"]
cpuInput =random.choice(randomChoices)
print(cpuInput)

if userInput == "snake" and cpuInput =="water":
  print("you wins")
if userInput == "water" and cpuInput== "snake":
  print("CPU wins")

if userInput == "gun" and cpuInput =="snake":
  print("you wins")
if userInput == "snake" and cpuInput== "gun":
  print("CPU wins")

if userInput == "water" and cpuInput =="gun":
  print("you wins")
if userInput == "gun" and cpuInput== "water":
  print("CPU wins")

if userInput==cpuInput or cpuInput==userInput:
  print("Draw")