# -*- coding: utf-8 -*-
"""
Created on Sun May 19 08:37:50 2019

@author: VIJ Global
"""

class location(object):
    def __init__(self, x, y):
        # x and y are floats
        self.x = x
        self.y = y
        
    def move(self, deltaX, deltaY):
        #deltaX and deltaY are floats
        return location(self.x + deltaX, self.y + deltaY)
    
    def getX(self):
        return self.x
    
    def getY(self):
        return self.y
    
    def distFrom(self, other):
        ox = other.x
        oy = other.y
        xDist = self.x - ox
        yDist = self.y - oy
        return (xDist**2 + yDist**2)**0.5
    
    def __str__(self):
        return '< ' + str(self.x) + ', ' + str(self.y) + '>'
    
class field(object):
    def __init__(self):
        self.drunks = {}
        
    def addDrunk(self, drunk, loc):
        if drunk in self.drunks:
            raise ValueError('Duplicate drunk')
        else:
            self.drunks[drunk] = loc
            
    def getLoc(self, drunk):
        if drunk not in self.drunks:
            raise ValueError('Drunk not in  fiels')
        return self.drunks[drunk]
    
    def moveDrunk(self, drunk):
        if drunk not in self.drunks:
            raise ValueError('Drunk not in the fiels')
        xDist, yDist = drunk.takeStep()
        currentLocation = self.drunks[drunk]
        #use move method of location to get new location
        self.drunks[drunk] = currentLocation.move(xDist, yDist)


class Drunk(object):
    def __init__(self, name):
        self.name = name
    
    def __str__(self):
        return 'This drunk is named ' + self.name
 
       
import random
class usualDrunk(Drunk):
    def takeStep(self):
        stepChoices = [(0.0, 1.0), (0.0, -1.0), (1.0, 0.0), (-1.0, 0.0)]
        return random.choice(stepChoices)
 
    
class coldDrunk(Drunk):
    def takeStep(self):
        stepChoices = [(0.0, 0.9), (0.0, -1.1),(1.0, 0.0), (-1.0, 0.0)]
        return random.choice(stepChoices)
 
    
def walk(f, d, numSteps):
    #assumes: f a field, d a drunk in f, and numSteps an int >= 0
    #moves  d numSteps times; returns the distance between the final 
    #location and the location at the start of the walk.
    
    start = f.getLoc(d)
    for s in range(numSteps):
        f.moveDrunk(d)
    return start.distFrom(f.getLoc(d))

def simWalks(numSteps, numTrials, dClass):
    #assumes numSteps an int >= 0, numTrials an int > 0, dClass a subclass of Drunk
    #simulates numTrials walks of numSteps steps each. return a list of the final distances
    # for each trial    
    homer = dClass(Drunk)
    origin = location (0, 0)
    distances = []
    for t in range(numTrials):
        f = field()
        f.addDrunk(homer, origin)
#        print(walk(f, homer, 0))
#        print(walk(f, homer, 1))
#        assert False
        distances.append(round(walk(f, homer, numSteps), 1))
    return distances

def drunkTest(walkLengths, numTrials, dClass):
    #assumes walkLEngths a sequence of ints >= 0 numTrials an int > 0,
    #dClass a subclass of of Drunk
    #for each number of steps in walkLengths, runs simWalks with numTrials walks
    #and print results
    for numSteps in walkLengths:
        distances = simWalks(numSteps, numTrials, dClass)
        print(dClass.__name__, ' radom walk of ', numSteps, ' steps')
        print('Mean = ', round(sum(distances)/len(distances), 4))
        print('Max = ', max(distances), ' Min = ', min(distances))
        
def simAll(drunkKinds, walkLengths, numTrials):
    for dClass in drunkKinds:
        drunkTest(walkLengths, numTrials, dClass)


#random.seed(0)
#drunkTest((10, 100, 1000, 10000), 100, usualDrunk)
#drunkTest((0, 1, 2, 3), 100, usualDrunk)
#simAll((usualDrunk, coldDrunk), (1, 10, 100, 1000, 10000), 100)


class styleIterator(object):
    def __init__(self, styles):
        self.index = 0
        self.styles = styles
        
    def nextStyle(self):
        result = self.styles[self.index]
        if self.index == len(self.styles) - 1:
            self.index = 0
        else:
            self.index += 1
        return result
    
def simDrunk(numTrials, dClass, walkLengths):
    meanDistances = []
    for numSteps in walkLengths:
        print('Starting simulation of ', numSteps, ' steps')
        trials = simWalks(numSteps, numTrials, dClass)
        mean = sum(trials)/len(trials)
        meanDistances.append(mean)
    return meanDistances

import pylab

def SimAll(drunkKinds, walkLengths, numTrials):
    styleChoice = styleIterator(('m-', 'b--', 'g-.'))
    for dClass in drunkKinds:
        curStyle = styleChoice.nextStyle()
        print('Starting simulation of ', dClass.__name__)
        means = simDrunk(numTrials, dClass, walkLengths)
        pylab.plot(walkLengths, means, curStyle, label = dClass.__name__)
    pylab.title('Mean Distance from Origin (' + str(numTrials) + ' trials)' )
    pylab.xlabel('Number of Steps')
    pylab.ylabel('Distance from Origin')
    pylab.legend(loc = 'best')
    
#numSteps = (10, 100, 1000, 10000)
#SimAll((usualDrunk, coldDrunk), numSteps, 100)
    
def getFinalLocs(numSteps, numTrials, dClass):
    locs =[]
    d = dClass(Drunk)
    for t in range(numTrials):
        f = field()
        f.addDrunk(d, location(0, 0))
        for s in range (numSteps):
            f.moveDrunk(d)
        locs.append(f.getLoc(d))
    return locs

def plotLocs(drunkKinds, numSteps, numTrials):
    styleChoice = styleIterator(('k+', 'r^', 'mo '))
    for dClass in drunkKinds:
        locs = getFinalLocs(numSteps, numTrials, dClass)
        xVals, yVals = [], []
        for loc in locs:
            xVals.append(loc.getX())
            yVals.append(loc.getY())
        xVals = pylab.array(xVals)
        yVals = pylab.array(yVals)
        meanX = sum(abs(xVals))/len(xVals)
        meanY = sum(abs(yVals))/len(yVals)
        curStyle = styleChoice.nextStyle()
        pylab.plot(xVals, yVals, curStyle, label = dClass.__name__ + ' mean abs dist = < ' + str(meanX) + ', ' + str(meanY) + '>' )
    pylab.title('Location at End of Walds (' + str(numSteps) + ' steps)' )
    pylab.ylim(-1000, 1000)
    pylab.xlim(-1000, 1000)
    pylab.xlabel('Steps East/West of Origin')
    pylab.ylabel('Steps Noth/South of Origin')
    pylab.legend(loc = 'upper left')
    
#random.seed(0)
#plotLocs((usualDrunk, coldDrunk), 10000, 1000)


class oddField(field):
    def __init__(self, numHoles = 1000, xRange = 100, yRange = 100):
        field.__init__(self)
        self.wormHoles = {}
        for w in range (numHoles):
            x = random.randint(-xRange, xRange)
            y = random.randint(-yRange, yRange)
            newX = random.randint(-xRange, xRange)
            newY = random.randint(-yRange, yRange)
            newLoc = location(newX, newY)
            self.wormHoles[(x, y)] = newLoc
            
def MoveDrunk(self, drunk):
    field.MoveDrunk(self, drunk)
    x = self.drunks[drunk].getX()
    y = self.drunks[drunk].getY()
    if (x, y) in self.wormHoles:
        self.drunks[drunk] = self.wormHoles[(x, y)]
            
def traceWalk(fieldKinds, numSteps):
    styleChoice = styleIterator(('b+', 'r^', 'ko'))
    for fClass in fieldKinds:
        d = usualDrunk(Drunk)
        f = fClass()
        f.addDrunk(d, location(0, 0))
        locs = []
        for s in range (numSteps):
            f.moveDrunk(d)
            locs.append(f.getLoc(d))
        xVals, yVals = [], []
        for loc in locs:
            xVals.append(loc.getX())
            yVals.append(loc.getY())
            curStyle = styleChoice.nextStyle()
            pylab.plot(xVals, yVals, curStyle, label = fClass.__name__)
            pylab.title('Spots Visited on Walk (' + str (numSteps) + ' steps)' )
            pylab.xlabel('Steps East/West of Origin')
            pylab.ylabel('Steps North/South of Origin')
            pylab.legend(loc = 'best')
        
#traceWalk((field, oddField), 500)

#random.seed(9001)
#for i in range(random.randint(1, 10)):
#    print(random.randint(1, 10))
#    
#random.seed(9001)
#d = random.randint(1, 10)
#for i in range(random.randint(1, 10)):
#    print(d)

random.seed(9001)
d = random.randint(1, 10)
for i in range(random.randint(1, 10)):
    if random.randint(1, 10) < 7:
        print(d)
    else:
        random.seed(9001)
        d = random.randint(1, 10)
        print(random.randint(1, 10))








