# -*- coding: utf-8 -*-
"""
Created on Sun Feb 10 18:51:45 2019

@author: VIJ Global
"""

value = input("Please think of a number between 0 and 100!: ")
low = 0
high = 100
guess = (low+high)//2
averageDifference = 0
while abs(guess-int(value)) >= averageDifference:
    print ("Is your secret number: ", guess, "?")
    answer = input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly. ")
    if answer == 'h':
        high = guess
    elif answer == 'l':
        low = guess
    elif answer == 'c':
        break
    elif answer != 'h' or answer != 'l' or answer != 'c':
        print ("please, invalid input")
    guess = (low+high)//2
print("Game over. Your secret number was: ", guess)