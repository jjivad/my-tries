# -*- coding: utf-8 -*-
"""
Created on Sun May  5 00:37:38 2019

@author: VIJ Global
"""
#problem 3

def greedySum(L, s):
    """ input: s, positive integer, what the sum should add up to
               L, list of unique positive integers sorted in descending order
        Use the greedy approach where you find the largest multiplier for 
        the largest value in L then for the second largest, and so on to 
        solve the equation s = L[0]*m_0 + L[1]*m_1 + ... + L[n-1]*m_(n-1)
        return: the sum of the multipliers or "no solution" if greedy approach does 
                not yield a set of multipliers such that the equation sums to 's'
    """
    multipliers = []
    remain = s
    for i in L:
        if i <= remain:
            mult = remain // i
            multipliers.append(mult)
            remain -= i * mult
        else:
            multipliers.append(0)
    sum1 = 0
    for j in range(len(multipliers)):
        sum1 += L[j]*multipliers[j]
    if sum1 == s:
        return sum(multipliers)
    else:
        return 'no solution'
    
# problem 7
def solveit(test):
    """ test, a function that takes an int parameter and returns a Boolean
        Assumes there exists an int, x, such that test(x) is True
        Returns an int, x, with the smallest absolute value such that test(x) is True 
        In case of ties, return any one of them. 
    """
    # IMPLEMENT THIS FUNCTION
    n = 0
    while True:
        if test(n) == True:
            return n
        elif test(-n) == True:
            return -n
        n += 1
        
        
#ignore everything below for submission
#### This test case prints 49 ####
        """
def f(x):
    return (x+15)**0.5 + x**0.5 == 15
print(solveit(f))

#### This test case prints 0 ####
def f(x):
    return x == 0
print(solveit(f))
"""
def solve(s):
    """ 
    s: positive integer, what the sum should add up to
    Solves the following optimization problem:
        x1 + x2 + x3 + x4 is minimized 
        subject to the constraint x1*25 + x2*10 + x3*5 + x4 = s
        and that x1, x2, x3, x4 are non-negative integers.
    Returns a list of the coefficients x1, x2, x3, x4 in that order
    """
    """
    Sum = 0
    sLeft = s
    L = []
    j = 1
    
    for i in reversed(range(0, 26, 5)):
    #for i in reversed(range(0, s+1, 5)):
        if i == 0:
            print('')
            print('first element is: ', i)
        else:
            L.append(sLeft//i)
        
            print('')
            print(i)
            print ('current list is = ', L)
            j += 1
            Sum += L[i - (i - j)] + (i * (sLeft//i))
            sLeft -= L[i - (i - j)] + (i * (sLeft//i))
            
            print ('sum = ', Sum, ' and sLeft = ', sLeft)
            if sLeft <= 0:
                return L
    return L
    """
    x1 = 0
    x2 = 0
    x3 = 0
    x4 = 0
    sCopy = s
    #sCheck = []
    """
    while sCopy >= 0:
        if sCopy >= 25:
            x1 = sCopy//25
            print('x1= ', x1, ' remain = ', sCopy - (x1*25))
        elif sCopy >= 10:
            x2 = sCopy//10
            print('x2= ', x2, ' remain = ', sCopy - (x2*10))
        elif sCopy >= 5:
            x3 = sCopy//5
            print('x3= ', x3, ' remain = ', sCopy - (x3*5))
        elif sCopy >= 0:
            x4 = sCopy
            print('x4= ', x4, ' remain = ', sCopy - x4)
        
        sCopy = sCopy - ((x1*25)+(x2*10)+(x3*5)+x4)
        print('remainder = ', sCopy)
        L = [x1, x2, x3, x4]
    return L
    """
    """
    #for i in reversed(range(0, s)):
    while sCopy >= 0:
        if sCopy >= 25:
            x1 = sCopy//25
            sCopy -= (x1*25)
            print('i =', 25, ' x1=', x1, ' remain = ', sCopy)
        else:
            if sCopy >= 10:
                x2 = sCopy//10
                sCopy -= (x2*10)
                print('i = ', 10, 'x2= ', x2, ' remain = ', sCopy)
            else:
                if sCopy >= 5:
                    x3 = sCopy//5
                    sCopy -= (x3*5)
                    print('i = ', 5, 'x3= ', x3, ' remain = ', sCopy)
                else:
                    if sCopy >= 0:
                        x4 = sCopy
                        print('i = ', 1, 'x4= ', x4, ' remain = ', sCopy - x4)
                    else:
                        return 'no solution'
        #if sCopy <= 0:
            #break
        sCopy -= sCopy
        print('copy is ',sCopy)
        L = [x1, x2, x3, x4]        
    return L
    """
    L = []
    check = 0
    remain = s
    for i in [25, 10, 5, 1]:
        
        if remain >= 0:
            L.append(remain//i)
            check = (i*(remain//i))
            remain = remain - check
            print('check = ', check, ' remain = ', remain)
            
            
    return L
          
test = solve(255)
print (test)
        










