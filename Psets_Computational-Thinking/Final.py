# -*- coding: utf-8 -*-
"""
Created on Wed Apr 24 04:25:39 2019

@author: VIJ Global
"""

# problem 1
"""
1) Consider deriving the probability of a coin 
flip coming up heads by running m trials of 100 
flips each. If the coin is fair, the mean probability 
of the m trials will go to 0.5 as m goes to infinity.

True correct


2) Consider two normal distributions, A and B. The standard deviation of A is 3 and the standard deviation of B is 5. For each distribution, 1,000 observations are drawn and plotted in a histogram with 10 bins, creating one histogram for each distribution.

???incorrect, The rightmost bin of A will have 
fewer points than the rightmost bin of B. 


3) You roll an unfair (weighted) die. The distribution of the numbers rolled is a uniform distribution.

False correct

4) A simulation

All of the above correct

5) ???? Neither of the above incorrect _____-overfitting

6) If the R^2 of a model produced using linear regression is 0.7, the model accounts for 70% of the variance in the observations.

True correct

7) Given a finite set of data points there exists a polynomial fit such that the polynomial curve goes through each point in the data.

False correct

8) You want to calculate confidence intervals by applying the empirical rule, which requires that you have a normal distribution with a known mean and standard deviation. Which approach can you use to estimate the mean and standard deviation that you need? Choose all that work.

Central Limit Theorem, which requires that you have many sufficiently large samples from the population
Standard Error, which requires that you have one sufficiently large sample
correct
"""

# problem 2
import random, pylab
xVals = []
yVals = []
wVals = []
for i in range(1000):
    xVals.append(random.random())
    yVals.append(random.random())
    wVals.append(random.random())
xVals = pylab.array(xVals)
yVals = pylab.array(yVals)
wVals = pylab.array(wVals)
xVals = xVals + xVals
zVals = xVals + yVals
tVals = xVals + yVals + wVals
"""
1) The values in tVals are most closely:
Distributed with a Gaussian distribution correct

2) The values in xVals are most closely:
Uniformly distributed correct

3) pylab.plot(xVals, zVals)

Graph 5 correct

4) pylab.plot(xVals, yVals)

Graph 4 correct

5) pylab.plot(xVals, sorted(yVals))

Graph 3 correct

6) pylab.plot(sorted(xVals), yVals)

Graph 2 correct

7) pylab.plot(sorted(xVals), sorted(yVals))

Graph 1 correct
"""

# problem 3
# 3-1
"""
 You have a bucket with 4 red balls and 4 green balls. You draw 3 balls out of the bucket. Assume that once you draw a ball out of the
 bucket, you don't replace it. What is the probability of drawing 3 balls of the same color? Answer the question in reduced fraction
 form - eg 1/5 instead of 2/10.

 1/7
 correct
"""
# 3-2, Monte Carlo simulation
import random

# Paste your code here
def drawing_without_replacement_sim(numTrials):
    '''
    Runs numTrials trials of a Monte Carlo simulation
    of drawing 3 balls out of a bucket containing
    4 red and 4 green balls. Balls are not replaced once
    drawn. Returns a float - the fraction of times 3 
    balls of the same color were drawn in the first 3 draws.
    '''
    # Your code here
    counter = 0
    for i in range(numTrials):
        bucket = ['R', 'R', 'R', 'R', 'G', 'G', 'G', 'G']
        picks = []
        for j in range(3):
            k = random.choice(bucket)
            picks.append(k)
            bucket.remove(k)
        if picks[0] == picks[1] == picks[2]:
            counter += 1
    return counter/numTrials

# problem 4, 
# 4-1, make histogram
def makeHistogram(values, numBins, xLabel, yLabel, title=None):
    """
      - values, a list of numbers
      - numBins, a positive int
      - xLabel, yLabel, title, are strings
      - Produces a histogram of values with numBins bins and the indicated labels
        for the x and y axes
      - If title is provided by caller, puts that title on the figure and otherwise
        does not title the figure
    """

# Paste your entire function (including the definition) in the box.

# Restrictions:
# Do not paste import pylab in the box.
# You should only be using the pylab.hist, pylab.title, pylab.xlabel, pylab.ylabel, pylab.show functions from the pylab module.
# Do not leave any debugging print statements when you paste your code in the box.


# Paste your code here
def makeHistogram(values, numBins, xLabel, yLabel, title=None):
    """
      - values, a list of numbers
      - numBins, a positive int
      - xLabel, yLabel, title, are strings
      - Produces a histogram of values with numBins bins and the indicated labels
        for the x and y axes
      - If title is provided by caller, puts that title on the figure and otherwise
        does not title the figure
    """
    pylab.hist(values, bins = numBins)
    pylab.xlabel(xLabel)
    pylab.ylabel(yLabel)
    if title != None:
        pylab.title(title)
    pylab.show()
    
# 4-2, get Average
def getAverage(die, numRolls, numTrials):
    """
      - die, a Die
      - numRolls, numTrials, are positive ints
      - Calculates the expected mean value of the longest run of a number
        over numTrials runs of numRolls rolls.
      - Calls makeHistogram to produce a histogram of the longest runs for all
        the trials. There should be 10 bins in the histogram
      - Choose appropriate labels for the x and y axes.
      - Returns the mean calculated to 3 decimal places
    """

# A run of numbers counts the number of times the same dice value shows up in consecutive rolls. For example:
# a dice roll of 1 4 3 has a longest run of 1
# a dice roll of 1 3 3 2 has a longest run of 2
# a dice roll of 5 4 4 4 5 5 2 5 has a longest run of 3

# When this function is called with the test case given in the file, it will return 5.312. Your simulation may give slightly different
# values.

# Paste your entire function (including the definition) in the box.

# Restrictions:
# Do not import or use functions or methods from pylab, numpy, or matplotlib.
# Do not leave any debugging print statements when you paste your code in the box.
# If you do not see the return value being printed when testing your function, close the histogram window.


# Paste your code here
def getAverage(die, numRolls, numTrials):
    """
      - die, a Die
      - numRolls, numTrials, are positive ints
      - Calculates the expected mean value of the longest run of a number
        over numTrials runs of numRolls rolls
      - Calls makeHistogram to produce a histogram of the longest runs for all
        the trials. There should be 10 bins in the histogram
      - Choose appropriate labels for the x and y axes.
      - Returns the mean calculated to 3 decimal places
    """
    # TODO
    longest_runs = []
    for i in range(numTrials):
        rolls = [die.roll() for j in range(numRolls)]
        size = 1
        max_size = 0
        for i in range(len(rolls)-1):
            if rolls[i+1] == rolls[i]:
                size += 1
            else: 
                size = 1
            if max_size < size:
                max_size = size
        if max_size > 0:
            longest_runs.append(max_size)
        else:
            longest_runs.append(1)
    makeHistogram(longest_runs, numBins = 10, xLabel = 'Length of longest run', yLabel = 'frequency', title = 'Histogram of longest runs')
    return sum(longest_runs)/len(longest_runs)

# problem 5, 
"""
K-means is a greedy algorithm, meaning it looks for local minimum when choosing points closest 
to the centroid. For each dataset illustrated below, will k-means, 
as shown in lecture, using Euclidean distance as the metric be able 
to find clusters that match the dataset patterns?
1) Dataset 1 
No correct

2) Dataset 2
Yes correct

3) Dataset 3
No correct

4) Dataset 4
No correct

5) Dataset 5
Yes correct

6) Dataset 6
No correct
"""

# problem 6
def find_combination(choices, total):
    """
    choices: a non-empty list of ints
    total: a positive int
 
    Returns result, a numpy.array of length len(choices) 
    such that
        * each element of result is 0 or 1
        * sum(result*choices) == total
        * sum(result) is as small as possible
    In case of ties, returns any result that works.
    If there is no result that gives the exact total, 
    pick the one that gives sum(result*choices) closest 
    to total without going over.
    """
    
# Paste your entire function (including the definition) in the box. Note: If you 
#want to use numpy arrays, you should import numpy as np
# and use np.METHOD_NAME in your code. Unfortunately, pylab does not work with the grader.


import os
os.environ["OPENBLAS_NUM_THREADS"] = "1"
import numpy as np
import itertools

def find_combination(choices, total):
    """
    choices: a non-empty list of ints
    total: a positive int
 
    Returns result, a numpy.array of length len(choices) 
    such that
        * each element of result is 0 or 1
        * sum(result*choices) == total
        * sum(result) is as small as possible
    In case of ties, returns any result that works.
    If there is no result that gives the exact total, 
    pick the one that gives sum(result*choices) closest 
    to total without going over.
    """
    power_set = []
    for i in itertools.product([1,0], repeat = len(choices)):
        power_set.append(np.array(i))
    filter_set_eq = []
    filter_set_less = []
    for j in power_set:
        if sum(j*choices) == total:
            filter_set_eq.append(j)
        elif sum(j*choices) < total:
            filter_set_less.append(j)
    if len(filter_set_eq) > 0:
        minidx = min(enumerate(filter_set_eq), key=lambda x:sum(x[1]))[1]
        return minidx
    else:
        minidx = max(enumerate(filter_set_less), key = lambda x:sum(x[1]))[1]
        return minidx
    
# problem 7
"""
1) Using the Manhattan distance and looking only at "Income" and "Distance from North Pole", which two people are closest and farthest?

??? closest: Person 3 and Person 4 ||| farthest: Person 5 and Person 6 incorrect

2) If we were to cluster the people, the inclusion/exclusion of which feature would never impact the final clusters?

Continents Visited correct
"""

# problem 8
# 8-1, simulate growth of fox and rabbit population in a forest
def rabbitGrowth():
    """ 
    rabbitGrowth is called once at the beginning of each time step.
    It makes use of the global variables: CURRENTRABBITPOP and MAXRABBITPOP.
    The global variable CURRENTRABBITPOP is modified by this procedure.
    For each rabbit, based on the probabilities in the problem set write-up, 
      a new rabbit may be born.
    Nothing is returned.
    """
    # you need this line for modifying global variables
    global CURRENTRABBITPOP

    # TO DO
    #pass
    for i in range(CURRENTRABBITPOP):
        if random.random() <= (1 - (CURRENTRABBITPOP/MAXRABBITPOP)):
            CURRENTRABBITPOP += 1
            
def foxGrowth():
    """ 
    foxGrowth is called once at the end of each time step.
    It makes use of the global variables: CURRENTFOXPOP and CURRENTRABBITPOP,
        and both may be modified by this procedure.
    Each fox, based on the probabilities in the problem statement, may eat 
      one rabbit (but only if there are more than 10 rabbits).
    If it eats a rabbit, then with a 1/3 prob it gives birth to a new fox.
    If it does not eat a rabbit, then with a 1/10 prob it dies.
    Nothing is returned.
    """
    # you need these lines for modifying global variables
    global CURRENTRABBITPOP
    global CURRENTFOXPOP

    # TO DO
    #pass
    for i in range(CURRENTFOXPOP):
        if CURRENTRABBITPOP > 10:
            if random.random() <= (CURRENTRABBITPOP/MAXRABBITPOP):
                CURRENTRABBITPOP -= 1
                # fox reproducing
                if random.random() <= (1/3):
                    CURRENTFOXPOP += 1
        else:
            # fox dying
            if random.random() <= 0.1:
                CURRENTFOXPOP -= 1
            
def runSimulation(numSteps):
    """
    Runs the simulation for `numSteps` time steps.
    Returns a tuple of two lists: (rabbit_populations, fox_populations)
      where rabbit_populations is a record of the rabbit population at the 
      END of each time step, and fox_populations is a record of the fox population
      at the END of each time step.
    Both lists should be `numSteps` items long.
    """

    # TO DO
    #pass
    rabbits = []
    foxes = []
    for i in range(numSteps):
        rabbitGrowth()
        foxGrowth()
        rabbits.append(CURRENTRABBITPOP)
        foxes.append(CURRENTFOXPOP)
    return rabbits, foxes

# 8-2, 
"""
1) At some point in time, there are more foxes than rabbits.

True correct

2) The polyfit curve for the rabbit population is:

??? A straight line incorrect

3) The polyfit curve for the fox population is:

??? A concave up curve (looks like a U shape)incorrect

4) Changing the initial conditions from 500 rabbits and 30 foxes to 
50 rabbits and 300 foxes changes the general shapes of both the polyfit 
curves for the rabbit population and fox population.

False correct

5) Let's say we make a change in the original simulation. That is, 
we are going to change one detail in the original simulation, but everything 
else will remain the same as it was explained in Problem 8 - Part A.

Now, if a fox fails in hunting, it has a 90 percent chance of dying 
(instead of a 10 percent chance, as in the original simulation).

Changing the probability of an unsuccessful fox dying from 10% to 90% changes 
the general shapes of both the polyfit curves for the rabbit population 
and fox population.

False correct

"""

# die.py
import random, pylab

# You are given this function
def getMeanAndStd(X):
    mean = sum(X)/float(len(X))
    tot = 0.0
    for x in X:
        tot += (x - mean)**2
    std = (tot/len(X))**0.5
    return mean, std

# You are given this class
class Die(object):
    def __init__(self, valList):
        """ valList is not empty """
        self.possibleVals = valList[:]
    def roll(self):
        return random.choice(self.possibleVals)

# Implement this -- Coding Part 1 of 2
def makeHistogram(values, numBins, xLabel, yLabel, title=None):
    """
      - values, a sequence of numbers
      - numBins, a positive int
      - xLabel, yLabel, title, are strings
      - Produces a histogram of values with numBins bins and the indicated labels
        for the x and y axis
      - If title is provided by caller, puts that title on the figure and otherwise
        does not title the figure
    """
    # TODO
    pylab.hist(values, bins = numBins)
    pylab.xlabel(xLabel)
    pylab.ylabel(yLabel)
    if title != None:
        pylab.title(title)
    pylab.show()
    
                    
# Implement this -- Coding Part 2 of 2
def getAverage(die, numRolls, numTrials):
    """
      - die, a Die
      - numRolls, numTrials, are positive ints
      - Calculates the expected mean value of the longest run of a number
        over numTrials runs of numRolls rolls
      - Calls makeHistogram to produce a histogram of the longest runs for all
        the trials. There should be 10 bins in the histogram
      - Choose appropriate labels for the x and y axes.
      - Returns the mean calculated to 3 decimal places
    """
    # TODO
    longest_runs = []
    for i in range(numTrials):
        rolls = [die.roll() for j in range(numRolls)]
        size = 1
        max_size = 0
        for i in range(len(rolls)-1):
            if rolls[i+1] == rolls[i]:
                size += 1
            else: 
                size = 1
            if max_size < size:
                max_size = size
        if max_size > 0:
            longest_runs.append(max_size)
        else:
            longest_runs.append(1)
    makeHistogram(longest_runs, numBins = 10, xLabel = 'Length of longest run', yLabel = 'frequency', title = 'Histogram of longest runs')
    return sum(longest_runs)/len(longest_runs)
        
    
# One test case
#print(getAverage(Die([1,2,3,4,5,6,6,6,7]), 500, 10000))
#print(getAverage(Die([1,2,3,4,5,6]), 50, 1000))
#print(getAverage(Die([1,2,3,4,5,6,6,6,7]), 1, 1000))

# rabit.py
import random
import pylab

# Global Variables
MAXRABBITPOP = 1000
CURRENTRABBITPOP = 500
CURRENTFOXPOP = 30

def rabbitGrowth():
    """ 
    rabbitGrowth is called once at the beginning of each time step.
    It makes use of the global variables: CURRENTRABBITPOP and MAXRABBITPOP.
    The global variable CURRENTRABBITPOP is modified by this procedure.
    For each rabbit, based on the probabilities in the problem set write-up, 
      a new rabbit may be born.
    Nothing is returned.
    """
    # you need this line for modifying global variables
    global CURRENTRABBITPOP

    # TO DO
    #pass
    for i in range(CURRENTRABBITPOP):
        if random.random() <= (1 - (CURRENTRABBITPOP/MAXRABBITPOP)):
            CURRENTRABBITPOP += 1
            
def foxGrowth():
    """ 
    foxGrowth is called once at the end of each time step.
    It makes use of the global variables: CURRENTFOXPOP and CURRENTRABBITPOP,
        and both may be modified by this procedure.
    Each fox, based on the probabilities in the problem statement, may eat 
      one rabbit (but only if there are more than 10 rabbits).
    If it eats a rabbit, then with a 1/3 prob it gives birth to a new fox.
    If it does not eat a rabbit, then with a 1/10 prob it dies.
    Nothing is returned.
    """
    # you need these lines for modifying global variables
    global CURRENTRABBITPOP
    global CURRENTFOXPOP

    # TO DO
    #pass
    for i in range(CURRENTFOXPOP):
        if CURRENTRABBITPOP > 10:
            if random.random() <= (CURRENTRABBITPOP/MAXRABBITPOP):
                CURRENTRABBITPOP -= 1
                # fox reproducing
                if random.random() <= (1/3):
                    CURRENTFOXPOP += 1
        else:
            # fox dying
            if random.random() <= 0.9:
                CURRENTFOXPOP -= 1
            
def runSimulation(numSteps):
    """
    Runs the simulation for `numSteps` time steps.
    Returns a tuple of two lists: (rabbit_populations, fox_populations)
      where rabbit_populations is a record of the rabbit population at the 
      END of each time step, and fox_populations is a record of the fox population
      at the END of each time step.
    Both lists should be `numSteps` items long.
    """

    # TO DO
    #pass
    rabbits = []
    foxes = []
    for i in range(numSteps):
        rabbitGrowth()
        foxGrowth()
        rabbits.append(CURRENTRABBITPOP)
        foxes.append(CURRENTFOXPOP)
    return rabbits, foxes

print(runSimulation(200))

# Plotting for Problem 8 Part B
def plotSimulation(numSteps):
    rabbits = []
    foxes = []
    for i in range(numSteps):
        rabbitGrowth()
        foxGrowth()
        rabbits.append(CURRENTRABBITPOP)
        foxes.append(CURRENTFOXPOP)
    pylab.plot(range(numSteps), rabbits, label = 'rabbits')
    rabbit_coeff = pylab.polyfit(range(numSteps), rabbits, 2)
    pylab.plot(pylab.polyval(rabbit_coeff, range(numSteps)))
    pylab.plot(range(numSteps), foxes, label = 'foxes')
    fox_coeff = pylab.polyfit(range(numSteps), foxes, 2)
    pylab.plot(pylab.polyval(fox_coeff, range(numSteps)))
    pylab.show()
    
plotSimulation(200)