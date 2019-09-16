# -*- coding: utf-8 -*-
"""
Created on Mon Feb 11 17:32:40 2019

@author: VIJ Global
"""

x = 9
differenceMin = 0.1
low = 0
guess = 0.0
guessTime = 0
while ((guess**2)-x) <= differenceMin:
    guessTime += 1
    if (guess**2) < x:
        low = guess
    else:
        break
    guess += 1
print ("square guess is: ", guess, "number of guessing: ", guessTime)