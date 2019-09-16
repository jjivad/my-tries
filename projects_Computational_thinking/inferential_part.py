# -*- coding: utf-8 -*-
"""
Created on Thu May 23 16:12:45 2019

@author: VIJ Global
"""

import random

class FairRoulette():
    def __init__(self):
        self.pockets = []
        for i in range(1, 37):
            self.pockets.append(i)
        self.ball = None
        self.blackOdds, self.redOdds = 1.0, 1.0
        self.pocketOdds = len (self.pockets) - 1.0
        
    def spin(self):
        self.ball = random.choice(self.pockets)
        
    def isBlack(self):
        if type(self.ball) != int:
            return False
        if ((self.ball > 0 and self.ball <= 10) or (self.ball > 18 and self.ball <= 28)):
            return self.ball % 2 == 0
        else:
            return self.ball % 2 == 1
        
    def isRed(self):
        return type(self.ball) == int and not self.isBlack()
    
    def betBlack(self, amt):
        if self.isBlack():
            return amt * self.blackOdds
        else:
            return -amt
        
    def betRed(self, amt):
        if self.isRed():
            return amt * self.redOdds
        else:
            return -amt * self.redOdds
        
    def betPocket(self, pocket, amt):
        if str(pocket) == str(self.ball):
            return amt * self.pocketOdds
        else:
            return -amt
        
    def __str__(self):
        return 'Fair roulette'
    
def playRoulette(game, numSpins, toPrint = True):
    luckyNumber = '2'
    bet = 1
    totRed, totBlack, totPocket = 0.0, 0.0, 0.0
    for i in range (numSpins):
        game.spin()
        totRed += game.betRed(bet)
        totBlack += game.betBlack(bet)
        totPocket += game.betPocket(luckyNumber, bet)
    if toPrint:
        print(numSpins, 'spins of', game)
        print('Expected return betting red = ', str(100 * totRed/numSpins) + '%')
        print('Expected return betting black = ', str(100 * totBlack/numSpins) + '%')
        print('Expected return betting ', luckyNumber, ' = ', str(100 * totPocket/numSpins) + '%\n')
    return (totRed/numSpins, totBlack/numSpins, totPocket/numSpins)

numSpins = 1000
game = FairRoulette()
playRoulette(game, numSpins)

class euRoulette(FairRoulette):
    def __init__(self):
        FairRoulette.__init__(self)
        self.pockets.append('0')
    
    def __str__(self):
        return 'European Roulette'
    
class amRoulette(FairRoulette):
    def __init__(self):
        FairRoulette.__init__(self)
        self.pockets.append('00')
    
    def __str__(self):
        return 'American Roulette'
    
def findPocketReturn(game, numTrials, trialSize, toPrint):
    pocketReturns = []
    for t in range(numTrials):
        trialVals = playRoulette(game, trialSize, toPrint)
        pocketReturns.append(trialVals[2])
    return pocketReturns

   
#random.seed(0)
#numTrials = 50000
#numSpins = 200
#game = FairRoulette()
#
#means = []
#for i in range(numTrials):
#    means.append(findPocketReturn(game, 1, numSpins)[0]/numSpins)
#
#pylab.hist(means, bins = 19,
#           weights = pylab.array(len(means)*[1])/len(means))
#pylab.xlabel('Mean Return')
#pylab.ylabel('Probability')
#pylab.title('Expected Return Betting a Pocket')
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
        
        
        
        
        
        