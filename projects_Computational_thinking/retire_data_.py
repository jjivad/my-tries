# -*- coding: utf-8 -*-
"""
Created on Tue May  7 15:08:25 2019

@author: VIJ Global
"""
import pylab as plt

def retire(monthly, rate, terms):
    savings = [0]
    base = [0]
    mRate = rate/12
    for i in range(terms):
        base += [i]
        savings += [savings[-1] *(1 + mRate) + monthly]
    return base, savings

def displayRetirementWithMonthlies(monthlies, rate, terms):
    plt.figure('retireMonth')
    plt.clf()
    #plt.ylim(0, 100)
    for monthly in monthlies:
        xvals, yvals = retire(monthly, rate, terms)
        plt.plot(xvals, yvals, label = 'retire: ' + str(monthly))
        plt.legend(loc = 'upper left')
        #plt.ylim(0, 100)
    
displayRetirementWithMonthlies([500, 600, 700, 800, 900, 1000, 1100], 0.05, 40*12)

def displayRetirementWithRates(month, rates, terms):
    plt.figure('retireRate')
    plt.clf()
    for rate in rates:
        xvals, yvals = retire(month, rate, terms)
        plt.plot(xvals, yvals, label = 'retire: ' + str(month) + ': ' + str(int(rate*100)))
        plt.legend(loc = 'upper left')
        
displayRetirementWithRates(800, [.03, .05, .07], 40 * 12)

def displayRetirementWithMonthsAndRates(monthlies, rates, terms):
    plt.figure('retireboth')
    plt.clf()
    plt.xlim(30*12, 40*12)
    for monthly in monthlies:
        for rate in rates:
            xvals, yvals = retire(monthly, rate, terms)
            plt.plot(xvals, yvals, label = 'retire: ' + str(monthly) + ': ' + str(int(rate*100)))
            plt.legend(loc = 'upper left')
            
displayRetirementWithMonthsAndRates([500, 700, 900, 1100], [.03, .05, .07], 40*12)

# to well visualize the graph
def displayRetirementWithMonthsAndRates2(monthlies, rates, terms):
    plt.figure('retirement')
    plt.clf()
    plt.xlim(30*12, 40*12)
    plt.ylim(0, 3000000) # just add it to view the graphs but the prof didn't have it
    monthLabels = ['r', 'b', 'g', 'k']
    rateLabels = ['-', '^', '--']
    for i in range(len(monthlies)):
        monthly = monthlies[i]
        monthLabel = monthLabels[i % len(monthLabels)]
        for j in range(len(rates)):
            rate = rates[j]
            rateLabel = rateLabels[j % len(rateLabels)]
            xvals, yvals = retire(monthly, rate, terms)
            plt.plot(xvals, yvals, monthLabel + rateLabel, label = 'retire: ' + str(monthly) + ': ' + str(int(rate*100)))
            plt.legend(loc = 'upper left')
            
displayRetirementWithMonthsAndRates2 ([500, 700, 900, 1100], [.03, 0.5, .07], 40*12)
            












