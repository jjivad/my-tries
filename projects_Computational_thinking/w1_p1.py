# -*- coding: utf-8 -*-
"""
Created on Wed Apr 17 04:14:05 2019

@author: VIJ Global
"""

"""
#exercise 1
def metric1 (item):
    return item.getValue()/item.getWeight()
def metric2 (item):
    return -item.getWeight()
def metric3 (item):
    return item.getValue()

#the big O to be identified
NUMBER = 3
def look_for_things(myList):
    #Looks at all elements
    for n in myList:
        if n == NUMBER:
            return True
    return False

def get_all_subsets(some_list):
    #Returns all subsets of size 0 - len(some_list) for some_list
    if len(some_list) == 0:
        # If the list is empty, return the empty list
        return [[]]
    subsets = []
    first_elt = some_list[0]
    rest_list = some_list[1:]
    # Strategy: Get all the subsets of rest_list; for each
    # of those subsets, a full subset list will contain both
    # the original subset as well as a version of the subset
    # that contains first_elt
    for partial_subset in get_all_subsets(rest_list):
        subsets.append(partial_subset)
        next_subset = partial_subset[:] + [first_elt]
        subsets.append(next_subset)
    return subsets

NUMBER = 3
def look_for_all_the_things(myList):
    #Looks at all subsets of this list
    # Make subsets
    all_subsets = get_all_subsets(myList)
    for subset in all_subsets:
        if sum(subset) == NUMBER:
            return True
    return False

NUMBER = 3
def look_for_other_things(myList):
    #Looks at all pairs of elements
    for n in myList:
        for m in myList:
            if n - m == NUMBER or m - n == NUMBER:
                return True
    return False

"""
#greedy algorithms
class Food(object):
    def __init__(self, n, v, w):
        self.name = n
        self.value = v
        self.calories = w
        
    def getValue(self):
        return self.value
    
    def getCost(self):
        return self.calories
    
    def density(self):
        return self.getValue()/self.getCost()
    
    def __str__(self):
        return self.name + ': <' + str(self.value) + ', ' + str(self.calories) + '>'

def buildMenu(names, values, calories):
    menu = []
    for i in range (len(values)):
        menu.append(Food(names[i], values[i], calories[i]))
    return menu
    

def greedy (items, maxCost, keyFunction):
        #names, values, calories lists of same length.
        #name a list of strings
        #values and calories lists of numbers
        #returns list of foods
        
        #items a list, maxCost >= 0
        #keyFunction maps elements of items to numbers  
    result = []
    totalValue, totalCost = 0.0, 0.0
    itemsCopy = sorted(items, key = keyFunction, reverse = True)
        
    for i in range(len(itemsCopy)):
        if (totalCost + itemsCopy[i].getCost()) <= maxCost:
            result.append(itemsCopy[i])
            totalCost += itemsCopy[i].getCost()
            totalValue += itemsCopy.getValue()
    return (result, totalValue)

def testGreedy(items, constraint, keyFunction):
    taken, val = greedy(items, constraint, keyFunction)
    print('total value of items taken = ', val)
    for item in taken:
        print('  ', item)
    
def greedys(foods, maxUnits):
    print('Use greedy by value to allocate ', maxUnits, ' calories')
    testGreedy(foods, maxUnits, Food.getValue)
        
    print('use greedy by cost to allocate ', maxUnits, ' calories')
    testGreedy(foods, maxUnits, lambda x: 1/Food.getCost(x))
        
    print('Use greedy by density to allocate ', maxUnits, ' calories')
    testGreedy(foods, maxUnits, Food.density)
    
def maxVal(toConsider, avail):
    if toConsider == [] or avail == 0:
        result = (0, ())
    elif toConsider[0].getValue() > avail:
        result = maxVal(toConsider[1:], avail)
    else:
        nextItem = toConsider[0]
        withVal, withToTake = maxVal(toConsider[1:], avail - nextItem.getValue())
        withVal += nextItem.getValue()
        withoutVal, withoutToTake = maxVal(toConsider[1:], avail)
        if withVal > withoutVal:
            result = (withVal, withToTake + (nextItem,))
        else:
            result = (withoutVal, withoutToTake)
    return result

def FastMaxVal (toConsider, avail, memo = {}):
    if (len(toConsider), avail) in memo:
        result = memo[(len(toConsider), avail)]
    elif toConsider == [] or avail == 0:
        result = (0, ())
    elif toConsider[0].getCost() > avail:
        result = FastMaxVal(toConsider[1:], avail, memo)
    else:
        nextItem = toConsider[0]
        #explore left brach
        withVal, withToTake = FastMaxVal(toConsider[1:], avail - nextItem.getCost(), memo)
        withVal += nextItem.getValue()
        withoutVal, withoutToTake = FastMaxVal(toConsider[1:], avail, memo)
        #choose better branch
        if withVal > withoutVal:
            result = (withVal, withToTake + (nextItem, ))
        else:
            result = (withoutVal, withoutToTake)
    memo[(len(toConsider), avail)] = result
    return result

def testMaxVal (foods, maxUnits, algorithm, printItems = True):
    print('Menu contains ', len(foods), ' items')
    print('Use search tree to allocate ', maxUnits, ' calories')
    val, taken = algorithm(foods, maxUnits)
    if printItems:
        print('Total value of items taken = ', val)
        for item in taken:
            print(' ', item)

import random
def largeMenu (numIntems, maxVal, maxCost):
    items = []
    for i in range(numItems):
        items.append(Food(str(1), random.randint(1, maxVal), random.randint(1, maxCost)))
    return items 
           
for numItems in (5, 10, 15, 20, 25, 30, 35, 40, 45):
    items = largeMenu(numItems, 90, 250)
    testMaxVal(items, 750, FastMaxVal, False)            
        
    


names = ['wine', 'beer', 'pizza', 'burger', 'fries', 'cola', 'apple', 'donut', 'cake']
values = [89, 98, 95, 108, 90, 79, 58, 10]
calories = [123, 154, 258, 354, 305, 150, 95, 195]  
foods = Food(names, values, calories)

print(foods)

greedys(foods, 750)
print('')
maxVal(foods, 750)

#import random
#
#def largeMenu (numIntems, maxVal, maxCost):
#    items = []
#    for i in range(numItems):
#        items.append(Food(str(1), random.randint(1, maxVal), random.randint(1, maxCost)))
#    return items
#
#for numItems in (5, 10, 15, 20, 25, 30, 35, 40, 45):
#    items = largeMenu(numItems, 90, 250)
#    maxVal(items, 750, False)   
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    