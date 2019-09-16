# -*- coding: utf-8 -*-
"""
Created on Sun Apr 21 11:18:13 2019

@author: VIJ Global
"""
# Fibonnaci
def fibn():
    fib_1 = 0
    fib_2 = 1
    while True:
        next = fib_1 + fib_2
        yield next
        fib_1 = fib_2
        fib_2 = next
        print('fib1 is: ' , fib_1, ' fib2 is: ', fib_2)
        #if next == 100:
            #break
   # return next

#a = 0
#b = 1
#print(fibn(a,b))       
fib = fibn()
print(fib.__next__())

# recursive Fibonnaci
def fibo(n):
    if n == 0 or n == 1:
        return 1
    else:
        return fibo(n-1) + fibo(n-2)
#print (fibo(6))
#for i in range(121):
#    print('fib (' + str(i) + ' ) = ', fibo(i))
        
# Fibonnaci using memoization
# dynamic programming works in 2 things: optimal substructure and overlapping subproblems
def fastFib(n, memo = {}):
    # n is an int and memo used only by recursive calls, will return Fibonnaci of n
    if n == 0 or n == 1:
        return 1
    try:
        return memo[0]
    except KeyError:
        result = fastFib(n-1, memo) + fastFib(n-2, memo)
        memo[n] = result
        return result
    
for i in range(121):
    print('fib (' + str(i) + ' ) = ', fastFib(i))    
    
    
# range things in 2 or more bags
def yieldAllCombos(items):
    """
        Generates all combinations of N items into two bags, whereby each 
        item is in one or zero bags.

        Yields a tuple, (bag1, bag2), where each bag is represented as a list 
        of which item(s) are in each bag.
    """
    # Your code here
    N = len(items)
    # enumerate the 2**N possible combinations
    for i in range(3**N):
        bag1 = []
        bag2 = []
        for j in range(N):
            # test bit jth of integer i
            if (i // 3**j) % 3 == 1:
                bag1.append(items[j])
            elif (i // 3** j) % 3 == 0:
                bag2.append(items[j])
        yield (bag1, bag2)

#how to generate numbers, IDs automatically
Person = []
class listID(Person):
    genID = 0
    def __init__(self, name):
        Person.__init__(self, name)
        self.numID = listID. genID
        listID.genID += 1
    def getNumID (self):
        return self.numID
    def __lt__(self, other):
        return self.genID < other.numID
    def speak (self, utterance):
        return (self.getLastName() + "says: " + utterance)
    
p1 = listID("Jessy Inga")
Person.setBirthday(p1, 7, 24, 94)
p2 = listID("Tati Wanda")
Person.setBirthday(p2, 5, 23, 93)
p3 = listID("Jaja Monica")
Person.setBirthday(p3, 6, 12, 92)

listIDList = [p1, p2, p3]