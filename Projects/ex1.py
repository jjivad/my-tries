# -*- coding: utf-8 -*-
"""
Created on Sun Feb 10 16:30:58 2019

@author: VIJ Global
"""

value = int (input("enter number between 1 and 100: "))
if value>= 100:
    value = int (input("your value is bigger than 100, try again: "))
elif value < 1:
    value = int (input("your value is less than 1, try again: "))
else:
    print ("nice choice, let me guess it!")
    
low = 1
high = 100
guess = (low+high)/2.0
averageDifference = 0.01
numGuess = 0
while abs(guess-value) >= averageDifference:
    numGuess += 1
    print ("Is your secret number: ", guess, "?")
    answer = input("enter 'h' to say the guess is too HIGH, 'l' to say is too LOW, 'c' to say is CORRECT: ")
    if answer == 'h':
        high = guess
    elif answer == 'l':
        low = guess
    elif answer == 'c':
        print ("the guess is correct, Well done!")
        break
    elif answer != 'h' or answer != 'l' or answer != 'c':
        print ("please, invalid input")
    guess = (low+high)/2.0
print("the final guess was: ", guess, "after ", numGuess, " times.")