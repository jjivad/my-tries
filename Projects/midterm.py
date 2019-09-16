# -*- coding: utf-8 -*-
"""
Created on Sat Feb 23 19:26:11 2019

@author: VIJ Global
"""
""" ____1________
x = "pi"
y = "pie"
x,y = y,x
print(x)

____2_____
def f(x):
    while x > 3:
        f(x+1)
    return f(x)
print(f(2))

____3_____
while i >= 0:
    while j >= 0:
        print(i, j)
______ ____    
def f(x):
    a = []
    while x > 0:
        a.append(x)
        f(x-1)
        return f(x)
print(f(2))

______p2___5____
stuff  = "iQ"
for thing in stuff:
   if thing == 'iQ':
      print("Found it")
_______p2 __6_-__--

def Square(x):
    return SquareHelper(abs(x), abs(x))

def SquareHelper(n, x):
    if n == 0:
        return 0
    return SquareHelper(n-1, x) + x
"""



"""
def deep_reverse(L):
    reverseL = []
    for i in reversed(L):
        reverseL.append(i)
    return reverseL
print(deep_reverse([[1, 2], [3, 4], [5, 6, 7]]))
"""
"""________p4___ correct____"""


"""
def deep_reverse(L):
    L= reversed(L)
    return L

L = [[1, 2], [3, 4], [5, 6, 7]]
print(deep_reverse(L))

"""



""" _______p3_______"""

def evalQuadratic(a, b, c, x):
   '''
   a, b, c: numerical values for the coefficients of a quadratic equation
   x: numerical value at which to evaluate the quadratic.
   '''
   return a*x**2 + b*x + c

def twoQuadratics(a1, b1, c1, x1, a2, b2, c2, x2):
    sumAll = evalQuadratic(a1,b1,c1,x1)+evalQuadratic(a2,b2,c2,x2)
    return sumAll

print(twoQuadratics(1.19,5.93,5.73,-9.06, -0.98,5.48,2.21,4.96))

"""on edx I have to use: print(twoQuadratics(a1, b1, c1, x1, a2, b2, c2, x2))"""































""" __________Problem 4_______

def deep_reverse(L):
    revL= L[::-1]
    b = []
    for i in revL:
        i = i[::-1]
        b.append(i)      
    return b
print(deep_reverse([[1, 2], [3, 4], [5, 6, 7]])) """
"""on edx I've tried with print and without print but in vain"""


""" P3 ____ L reversed____

def deep_reverse(L):
    L.reverse()
    for i in L:
        if (type(i) == list):
            i.reverse()
    return L
L = [[1, 2], [3, 4], [5, 6, 7]]
deep_reverse(L)
print(L) 
"""
"""______7______
def f(i):
    return i + 2

def g(i):
    return i > 5

def applyF_filterG(L, f, g):
    newL = []
    for i in L:
        if (g(f(i))) == True:
            newL.append(i)
    L[:] = newL
    if len(L) == 0:
        return -1
    else:
        return max(L)

L = [0, -10, 5, 6, -4]

print(applyF_filterG(L, f, g))
print(L)
"""


"""_____Q5____
def dict_invert(d):
    inv_d = {}
    for (k, v) in d.items():
        inv_d[v] = inv_d.get(v, [])
        inv_d[v].append(k)
        inv_d[v].sort()
    return inv_d
d = {30000: 30, 600: 30, 2: 10}
print(dict_invert(d))
"""

""" _________dictionaries_getting the key_________

aDict = { 'a': ['aardvark'], 'b': ['baboon'], 'c': ['coati']}

aDict['d'] = ['donkey']
aDict['d'].append('dog')
aDict['d'].append('dingo')

def biggest(aDict):
    listValue = []
    listValue = aDict.values()
    sumValue = 0
    keyValue =""
    for i in listValue:
        if len(i) > sumValue:
            sumValue = len(i)
            keyValue = aDict.keys(i)
    return keyValue 


def keysWithValue(aDict, target):
    list_keys = []
    list_keys = aDict.keys()
    for (k,v) in aDict
"""
"""
def f(x,y):
    return x*y
def score(word, f):
    word = "abcdefghijklmnopqrstuvwxyz"
    Score = 0
    num = 0
    for i in word:
        num += 1
        Score = Score + (word[i]*num)
        return Score
    

def max_val(t): 
    max(t,key = itemgetter(1))[0] 

t = (5, (1,2), [[1],[2]])
print(max_val(t))

"""






     