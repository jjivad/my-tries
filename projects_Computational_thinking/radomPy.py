# -*- coding: utf-8 -*-
"""
Created on Sun May 12 12:18:09 2019

@author: VIJ Global
"""

import random
#print (random.randint(1, 5))
#print (random.choice(['apple', 'cat', 'banana', 'Jessy']))
#for i in range(-1, 100):
#        x = random.randrange(-1, 101)
#        if x % 2 == 0:
#            print (x)
            



#evenList = []
##lastList = []  
##x = random.randrange(-1, 101)          
##while True:
##    if x % 2 == 0:
##        if x not in l:
##            print (x)
#
#for i in range(-1, 100):
#    x = random.randrange(-1, 100)
#    if x % 2 == 0:
#        if x not in evenList:
#            evenList.append(x)
#            print (x)
#print(evenList)

#def genEven():
#    # Returns a random number x, where 0 <= x < 100
#    for i in range(-1, 100):
#        x = random.randrange(-1, 101)
#        if x % 2 == 0:
#            return x
#        

# generate even numbers between 0 and 100 randomly
def genEven():
    '''
    Returns a random even number x, where 0 <= x < 100
    '''
    # Your code here
    evenList = [] 
    x = random.randrange(-1, 100)          

    for i in range(-1, 100):
        x = random.randrange(-1, 100)
        if x % 2 == 0:
            if x not in evenList:
                evenList.append(x)
                return (x)
            
    #return random.randrange(0, 100, 2)_____ a simple answer
#
#print(genEven)


def deterministicNumber():  #return a predited number between 9 and 21
#    x = random.randint(9, 21)
#    for i in range (9, 21):
#        if (x % 2) == 0:
#            return x
#            break
    return 16
        
print(deterministicNumber)

def stochasticNumber():
    return random.randrange(10, 21, 2)
    


random.seed(0) # help to generate the same sequence of result, then use 0 as a seed
# it allows you to do the same thing everytime...

def rollDie():
    #return a random int between 1 and 6
    return random.choice([1,2,3,4,5,6])

def testRoll(n=10):
    result = ''
    for i in range (n):
        result = result + str(rollDie())
    print (result)
    
def runSim(goal, numTrials):
    total = 0
    for i in range (numTrials):
        result = ''
        for j in range(len(goal)):
            result += str(rollDie())
        if result == goal:
            total += 1
    print ('Actual probality = ', round(1/(6**len(goal)), 8))
    estProbability = round(total/numTrials, 8)
    print('Estimated Probability = ', round(estProbability, 8))
    
#runSim('11111', 1000000)
#runSim('11111', 1000000)

def fracBoxCars(numTests):
    numBoxCars = 0.0
    for i in range(numTests):
        if rollDie() == 6 and rollDie() == 6:
            numBoxCars += 1
    return numBoxCars/numTests
print ('Frequency of double 6 = ', str(fracBoxCars(100000) * 100) + '%')
    

    
    
    
    
    
    
    
    
    
    
    
    
    
    