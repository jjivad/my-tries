# -*- coding: utf-8 -*-
"""
Created on Wed Feb  6 17:01:34 2019

@author: VIJ Global
"""

s = input ("enter your value: ")
valueLength = len(s)
readThrough = 0
numberVowels = 0
while readThrough<valueLength:
    vowel=s[readThrough]
    if vowel=='a' or vowel=='e' or vowel=='i' or vowel=='o' or vowel=='u':
        numberVowels=numberVowels+1
        readThrough=readThrough+1
print("The number of vowels: ",numberVowels)