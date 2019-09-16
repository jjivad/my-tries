# -*- coding: utf-8 -*-
"""
Created on Mon Feb 11 17:58:30 2019

@author: VIJ Global
"""
def square (guess)
x = 0.0
differenceMin = 0.1
low = 0.0
guessTime = 0
while (x-(guess**2)) <= differenceMin:
    guessTime += 1
    if x < (guess**2):
        low = x
    else:
        break
    x += 1
print ("square guess is: ", x, "number of guessing: ", guessTime)

return 