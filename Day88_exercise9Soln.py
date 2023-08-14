# Day 88

'''This is for windows'''
import os
from win32com.client import Dispatch
names = ["Nitin","Sonakshi", "Sonali", "Nikhil"]
for name in names:
   speak = Dispatch("SAPI.SpVoice").Speak
   speak(f'Shoutout to {name}')

'''
This is how i make python to speak any word :-
 from win32com.client import Dispatch
speak = Dispatch("SAPI.SpVoice").Speak
speak("This line will speak by Python Interpreter by installing module")
'''