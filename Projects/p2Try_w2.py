# -*- coding: utf-8 -*-
import random
import datetime
import string
import math

"""
Created on Wed Feb 13 17:02:07 2019

@author: VIJ Global
"""
""" ____Recursive way____"""
"""
def recursivePower(base, exp):
    if exp == 1:
        return base
    elif exp == 0:
        return base/base
    else:
        return base*recursivePower(base,exp-1)
print(iterPower(-2,0))
"""

""" ___iteration way____
def iterPower(base, exp):
    produit = 1
    while exp > 0:
        produit *= base
        exp -= 1
    return produit
print(iterPower(-3,0))
"""
"""______________tuples____________
def myTuples(aTup):
    aTup = (1,2,3,4,5,"Jessy",7,8,9)
    oddTuple = ()
    pairTuple = ()
    for t in aTup:
        if (t%2) != 0:
            oddTuple = oddTuple + ((t),)
            return (oddTuple)     
        else:
            pairTuple = pairTuple + ((t),)
            return (pairTuple)
        t += 1
print (myTuples(aTup)) 
 """ 
"""_____________tuples_____________
tup = (1,2,3,4,5,"Jessy",7,8,9)
t = len(tup)
print(t)
odd = ()
while t > 0:
    if (t%2) != 0:
        odd += tup([t],)
        print (odd)
    
"""  
"""  ____________Tuples_______________ 

oddTuple = ()
    for t in aTup:
        if (t%2) != 0:
            oddTuple = oddTuple + ((t),)
    return (oddTuple)
"""    
"""
L=[4,-8,12,-24,36,-44]
def myFunction(abs,L):
    testL=[]
    for e in range (len(L)):
        testL[e]=abs(L[e]/4)
    return testL
    print(testL)
 """   
    
"""____________dictionaries_getting the sum of the values_length___________

listValue = []
    listValue = aDict.values()
    sumValue = 0
    for i in listValue:
        sumValue = sumValue + len(i)
    return sumValue
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
"""


"""________guess check_____
iteration = 0
count = 0
while iteration < 5:
    for letter in "hello, world":
        count += 1
    print("Iteration " + str(iteration) + "; count is: " + str(count))
    iteration += 1 
"""

"""______guess check___ infinite loop_____
for iteration in range(5):
    count = 0
    while True:
        for letter in "hello, world":
            count += 1
        print("Iteration " + str(iteration) + "; count is: " + str(count))
"""
"""  _____ guess check____
for iteration in range(5):
    count = 0
    while True:
        for letter in "hello, world":
            count += 1
        print("Iteration " + str(iteration) + "; count is: " + str(count))
        break
""" 
""" _____guess check_____   
count = 0
phrase = "hello, world"
for iteration in range(5):
    index = 0
    while index < len(phrase):
        count += 1
        index += 1
    print("Iteration " + str(iteration) + "; count is: " + str(count)) 
"""
"""" _____guess check_____ 
count = 0
phrase = "hello, world"
for iteration in range(5):
    while True:
        count += len(phrase)
        break
    print("Iteration " + str(iteration) + "; count is: " + str(count))    
"""

"""________recurcive_______

a = int(input("number a: "))
b = int(input("number b: "))"""
"""
def mod (a,b):
    c = min(a,b)
    for i in range (c): 
        if a > b:
            if a%b == 0:
                return b
                break
            else:
                b -= 1
        else:
            if b%a == 0:
                return a
                break
            else:
                a -= 1
            
print (mod(40, 50))
"""
"""   
a = int(input("number a: "))
b = int(input("number b: "))
"""

"""______itterative_____

def mod (a,b):
    c = min(a,b)
    while c >= 1:
        if a%c == 0 and b%c == 0:
            return c
        else:
            c -= 1
print (mod(32,100))
""" 
"""__________exceptions______________"""

"""  
def fancy_divide(numbers,index):
    try:
        denom = numbers[index]
        for i in range(len(numbers)):
            numbers[i] /= denom
    except IndexError:
        print("-1")
    else:
        print("1")
    finally:
        print("0")
        
fancy_divide([0, 2, 4], 0)
fancy_divide([0, 2, 4], 1)
fancy_divide([0, 2, 4], 4)

"""
"""
def fancy_divide(numbers, index):
    try:
        denom = numbers[index]
        for i in range(len(numbers)):
            numbers[i] /= denom
    except IndexError:
        fancy_divide(numbers, len(numbers) - 1)
    except ZeroDivisionError:
        print("-2")
    else:
        print("1")
    finally:
        print("0")    
#fancy_divide([0, 2, 4], 1) 
#fancy_divide([0, 2, 4], 4)
fancy_divide([0, 2, 4], 0)
"""
""" 
def fancy_divide(numbers, index):
    try:
        try:
            denom = numbers[index]
            for i in range(len(numbers)):
                numbers[i] /= denom
        except IndexError:
            fancy_divide(numbers, len(numbers) - 1)
        else:
            print("1")
        finally:
            print("0")
    except ZeroDivisionError:
        print("-2")
#fancy_divide([0, 2, 4], 1)
fancy_divide([0, 2, 4], 4)
fancy_divide([0, 2, 4], 0)
"""
"""    
def fancy_divide(list_of_numbers, index):
   denom = list_of_numbers[index]
   return [simple_divide(item, denom) for item in list_of_numbers]

#def simple_divide(item, denom):
 #  return item / denom 
def simple_divide(item, denom):
    try :
        elt = item / denom
        return elt
    except ZeroDivisionError:
       return 0

#fancy_divide([0, 2, 4], 1) 
fancy_divide([0, 2, 4], 0)      
"""
"""
def normalize(numbers):
    max_number = max(numbers)
    for i in range(len(numbers)):
        numbers[i] /= float(max_number)
    return numbers 
    
    try:
      normalize([0, 0, 0])
except ZeroDivisionError:
      print('Invalid maximum element')
"""
"""
def normalize(numbers):
    max_number = max(numbers)
    assert(max_number != 0), "Cannot divide by 0"
    for i in range(len(numbers)):
        numbers[i]  /= float(max_number)
        assert(0.0 <= numbers[i] <= 1.0), "output not between 0 and 1"
    return numbers        
""" 
"""_______pset4______Q1 code succeeded________
       
word = "ami"
SCRABBLE_LETTER_VALUES = {
    'a': 1, 'b': 3, 'c': 3, 'd': 2, 'e': 1, 'f': 4, 'g': 2, 'h': 4, 'i': 1, 'j': 8, 'k': 5, 'l': 1, 'm': 3, 'n': 1, 'o': 1, 'p': 3, 'q': 10, 'r': 1, 's': 1, 't': 1, 'u': 1, 'v': 4, 'w': 4, 'x': 8, 'y': 4, 'z': 10
}
score = 0
for i in word:
    score = SCRABBLE_LETTER_VALUES.get(i) #without quotes it's for the value
    print("char: ", i, "value: ", score)
    """
"""    
for i in word:
    score = SCRABBLE_LETTER_VALUES.get('i') #with quotes it's for the number that the value represent (each char is 1)
    print("char: ", i, "value: ", score)
"""    
"""_______pset4______Q2 code succeeded__________

hand = {'a':1, 'q':1, 'l':2, 'm':1, 'u':1, 'i':1}
currentHand = hand.copy()
"""
""" making a word into a list then check another word to verify if it's char are included in 
    that list, if yes the letter will be removed and return the final list with the remaining
    chars
l = "aqllmui"
lis = list(l)
wrd = ""
print('list is: ', lis)
for i in word:
   lis.remove(i)
print(lis)
for i in lis:
    wrd += i
print(wrd) 
"""
"""
for i in word:
    currentHand.get[i] -= 1
    if currentHand[i] == 0:
        currentHand.pop(i)
print (currentHand)       
#for (v, i) in currentHand:
 # for i in word:
  #    currentHand = currentHand[v:i-1]
   #while l < len(word):
      #value = currentHand[i]
      #print("before ",value)
      #value = value - 1
      #print("after", value)
      #l += 1
    #currentHand.pop(i)        
    #return currentHand"""
"""_______pset4______Q3 code __________

wordList = ['ami','quail','aquel','amil','aami','lam','mil','miil','mille','alim',]
def check(word, hand, wordList):
    copyHand = hand.copy()
    m = ""
    for words in wordList:
        print ("words:", words)
        if words == word:
          for i in word:
            if i in copyHand:
                m = m + i
                if copyHand[i] == 0:
                    return False
                    break
                copyHand[i] -= 1
                print("m value: ", m)
                #print(len(m)) #print length of a string
                
                        
            else:
                print(i)
                return False
                break
          return True
    return False
                       
print(check(word, hand, wordList))

value = check(word, hand, wordList)
print("my value is", value)"""
"""    
for i in word:
        print("this is my word: ", i)
        #for i in word and :
        for i in hand:
            for word in wordList:
                print("word: ", word)
            return(True)
                       
    return(False)
"""
"""
def playHand(hand, wordList, n):
    
    displayHand(hand)
    totalScore = 0   
        # Ask user for input
    wordInput = input("Enter word, or a '.' to indicate that you are finished: ")
    for i in wordInput: 
        # If the input is a single period:
        if i == ".":    
            # End the game (break out of the loop)
            break
            
        # Otherwise (the input is not a single period):        
        else:
            # If the word is not valid:
            if isValidWord(wordInput, hand, wordList) == False:
                
                # Reject invalid word (print a message followed by a blank line)
                print("Invalid word, please try again")
                print()
                return playHand(hand, wordList, n)
            # Otherwise (the word is valid):
            else:
                # Tell the user how many points the word earned, and the updated total score, in one line followed by a blank line
                score = getWordScore(wordInput, n)
                totalScore = totalScore + score
                print(wordInput, "earned ", score, " points. Total: ", totalScore, " points" )
                print()
                # Update the hand 
                updateHand(hand, wordInput)
                newHand = displayHand
                if len(newHand) == 0:
                    print("Run out of letters. Total score: ", totalScore)
                    break                    
                #return playHand(hand, wordList, n)
    # Game is over (user entered a '.' or ran out of letters), so tell user the total score
    print("Total: ", totalScore, " points")
"""    
"""
    nRound = n
    for i in range (n): 
        if wordInput == '.':
            print("your total score is: ", totalScore)
            break
        elif nRound == 0:
            print("You're out of move!")
            print("your total score is: ", totalScore)
            break
        nRound -= 1 """

"""_______classes______clock example____
class Clock(object):
    def __init__(self, time):
        self.time = time
    def print_time(self):
        time = '6:30'
        print(self.time)

clock = Clock('5:30')
clock.print_time()

class Clock(object):
    def __init__(self, time):
	    self.time = time
    def print_time(self, time):
	    print(time)

clock = Clock('5:30')
clock.print_time('10:30')

class Clock(object):
    def __init__(self, time):
        self.time = time
    def print_time(self):
        print(self.time)

boston_clock = Clock('5:30')
paris_clock = boston_clock
paris_clock.time = '10:30'
boston_clock.print_time()

_______example_______
"""
"""
class Weird(object):
    def __init__(self, x, y): 
        self.y = y
        self.x = x
    def getX(self):
        return x 
    def getY(self):
        return y

class Wild(object):
    def __init__(self, x, y): 
        self.y = y
        self.x = x
    def getX(self):
        return self.x 
    def getY(self):
        return self.y

X = 7
Y = 8
#w1 = Weird(X, Y)
#print(w1.getX())
#print(w1.getY())
w2 = Wild(X, Y)
print(w2.getX())

w3 = Wild(17, 18)
print(w3.getX())
print(w3.getY())

w4 = Wild(X, 18)
print(w4.getX())
print(w4.getY())

X = w4.getX() + w3.getX() + w2.getX()
print(X)

print(w4.getX())

Y = w4.getY() + w3.getY()
Y = Y + w2.getY()
print(Y)

print(w2.getY())
"""
"""
class fraction(object):
    def __init__(self, numer, denom):
        self.numer = numer
        self.denom = denom
    def __str__(self):
        return str(self.numer) + '/' + str(self.denom)
    def getNumer(self):
        return self.numer
    def getDenom(self):
        return self.denom
    def __add___(self, other):
        numerNew = other.getDenom()* self.getNumer() \
        + other.getNumer() * self.getDenom()
        denomNew = other.getDenom() * self.getDenom()
        return fraction(numerNew, denomNew)
    def __sub__(self, other):
        numerNew = other.getDenom()* self.getNumer() \
        - other.getNumer() * self.getDenom()
        denomNew = other.getDenom() * self.getDenom()
        return fraction(numerNew, denomNew)
    
        
    
threeQuarters = fraction(3, 4)
oneHalf = fraction(1,2)
twoThird = fraction(2,3)
print(oneHalf)
print(twoThird)
print(threeQuarters)
oneHalf.getNumer()
#new = oneHalf + twoThird
#print(new)
newAdd = twoThird + threeQuarters
print(newAdd)
secondNew = twoThird - threeQuarters
print(secondNew)
#secondNew.convert()
#print(secondNew)
"""

"""
class intSet(object):
    def __init__(self):
        self.vals = []
    def insert (self, e):
        if not e in self.vals:
            self.vals.append(e)
    def member (self, e):
        return e in self.vals
    def remove (self, e):
        try:
            self.vals.remove(e)
        except:
            raise ValueError(str(e) + 'not found')
    def __str__(self):
        self.vals.sort()
        result = ''
        for e in self.vals:
            result = result + str(e) + ","
            return '(' + result[:-1] + ')'
"""
"""
class Coordinate(object):
    def __init__(self, x, y): 
        self.y = y
        self.x = x
    def getX(self):
        # Getter method for a Coordinate object's x coordinate.
        # Getter methods are better practice than just accessing an attribute directly
        return x 
    def getY(self):
        # Getter method for a Coordinate object's x coordinate.
        # Getter methods are better practice than just accessing an attribute directly
        return y
    def __str__(self):
        return '<' + str(self.getX()) + ',' + str(self.getY()) + '>'
    def __eq__(self, other):
        #to compare 2 coordinates
        if Coordinate != other:
            return False
        else:
            return True
    def __repr__(self):
        return 'Coordinate(' + str(self.getX()) + ',' + str(self.getY()) + ')'
        #return 'Coordinate({},{})'.format(self.getX(), self.getX())
c = Coordinate(2,-8)
print (c)
"""            
"""
class intSet(object):
#    An intSet is a set of integers
#    The value is represented by a list of ints, self.vals.
#    Each int in the set occurs in self.vals exactly once.

    def __init__(self):
        #Create an empty set of integers
        self.vals = []

    def insert(self, e):
#        Assumes e is an integer and inserts e into self
        if not e in self.vals:
            self.vals.append(e)

    def member(self, e):
#        Assumes e is an integer
#           Returns True if e is in self, and False otherwise
        return e in self.vals

    def remove(self, e):
        
#        Assumes e is an integer and removes e from self
#           Raises ValueError if e is not in self
           
           
        try:
            self.vals.remove(e)
        except:
            raise ValueError(str(e) + ' not found')

    def __str__(self):
#        Returns a string representation of self
        self.vals.sort()
        return '{' + ','.join([str(e) for e in self.vals]) + '}'
    def intersect(self,other):
        #for the common elements in both sets
        newIntSet = []
        for e in self.vals:
          if e in other:
            newIntSet.append(e)
        return newIntSet
        #return intSet({e for e in self if e in other})
        #return '{' + ','.join([str(e) for e in sorted(self) if e in other]) + '}'
#        
#        for e in intSet:
#            if e in other:
#                newIntSet.append(e)
#            else:
#                newIntSet = newIntSet
#        return newIntSet
#    
    def __len__(self):
        #to check the length of a set
        return len(self.vals)
"""
"""
class Animal(object):
    def __init__(self, age):
        self.age = age
        self.name = name
    def get_age(self):
        return self.age
    def get_name(self):
        return self.name
    def set_age(self, newage):
        self.age = newage
    def set_name(self, newname=""):
        self.name = newname
    def __str__(self):
        return "animal: " + str(self.name) + ":" + str(self.age)

class Cat(Animal):
    def speak(self):
        print("meow")
    def __str__(self):
        return "cat: " + str(self.name) + ":" + str(self.age)

class Rabbit(Animal):
    def speak(self):
        print("meep")
    def __str__(self):
        return "rabbit: " + str(self.name) + ":" + str(self.age)

class Person(Animal):
    def __init__(self, name, age):
        Animal.__init__(self, age)
        Animal.set_name(self, name)
        self.friends = []
    def get_friends(self):
        return self.friends
    def add_friends(self, fname):
        if fname not in self.friends:
            self.friends.append(fname)
    def speak(self):
        print("hello")
    def age_diff(self, other):
        diff = self.get_age() - other.get_age()
        if self.age > other.age:
            print(self.name, "is", diff, "years older than", other.name)
        else:
            print(self.name, "is", -diff, "years younger than", other.name)
    def __str__(self):
        return "person: " + str(self.name) + ":" + str(self.age)
    
class Student(Person):
    def __init__(self, name, age, major = None):
        Person.__init__(self, name, age)
        self.major = major
    def change_major(self, major):
        self.major = major
    def speak (self):
        r = random.random()
        if r < 0.25:
            print("I have homework")
        elif 0.25 <= r < 0.5:
            print("I need sleep")
        elif 0.5 <= r < 0.75:
            print("I should eat")
        else:
            print("I am watching tv")
    def __str__(self):
        return "student: " + str(self.name) + ":" + str(self.age) + ":" + str(self.major)
"""    

#example of spell
"""
class Spell(object):
    def __init__(self, incantation, name):
        self.name = name
        self.incantation = incantation

    def __str__(self):
        return self.name + ' ' + self.incantation + '\n' + self.getDescription()
              
    def getDescription(self):
        return 'No description'
    
    def execute(self):
        print(self.incantation)


class Accio(Spell):
    def __init__(self):
        Spell.__init__(self, 'Accio', 'Summoning Charm')
    def getDescription(self):
        return 'This charm summons an object to the caster, potentially over a significant distance.'
    
class Confundo(Spell):
    def __init__(self):
        Spell.__init__(self, 'Confundo', 'Confundus Charm')

    def getDescription(self):
        return 'Causes the victim to become confused and befuddled.'

def studySpell(spell):
    print(spell)

spell = Accio()
spell.execute()
studySpell(spell)
studySpell(Confundo())
print(Accio())        
"""        

#inheritance 
"""
class A(object):
    def __init__(self):
        self.a = 1
    def x(self):
        print("A.x")
    def y(self):
        print("A.y")
    def z(self):
        print("A.z")

class B(A):
    def __init__(self):
        A.__init__(self)
        self.a = 2
        self.b = 3
    def y(self):
        print("B.y")
    def z(self):
        print("B.z")

class C(object):
    def __init__(self):
        self.a = 4
        self.c = 5
    def y(self):
        print("C.y")
    def z(self):
        print("C.z")

class D(C, B):
    def __init__(self):
        C.__init__(self)
        B.__init__(self)
        self.d = 6
    def z(self):
        print("D.z")        
        
obj = D()        
print(obj.a)
print(obj.b)
print(obj.c)
print(obj.d)
obj.x()
obj.y()
obj.z()
"""
#for tagging, example of rabbit above
""" 
class Animal(object):
    def __init__(self,age):
        self.age = age
        self.name = name
    def get_age(self):
        return self.age
    def get_name(self):
        return self.name
    def set_age(self, newage):
        self.age = newage
    def set_name(self, newname=""):
        self.name = newname
    def __str__(self):
        return "animal: " + str(self.name) + ":" + str(self.age)
    
class Rabbit(Animal):
    tag = 1
    def __init__(self, age, parent1 = None, parent2 = None):
        Animal.__init__(self, age)
        self.parent1 = parent1
        self.parent2 = parent2
        self.rid = Rabbit.tag #to access the tag in the Rabbit class outside the def __init__
        Rabbit.tag += 1 # to incease the tag each time a new rabbit is created
    def get_rid(self):
        return str(self.rid).zfill(3)
    def get_parent1(self):
        return self.parent1
    def get_parrent2(self):
        return self.parent2
    def __add__(self, other):
        return Rabbit(0, self, other) # 0 represent the age, self for the parent 1 and the other for parent 2
    def __eq__(self, other):
        parents_same = self.parent1.rid == other.parent1.rid and self.parent2.rid == other.parent2.rid 
        parents_opposite = self.parent2.rid == other.parent1.rid and self.parent1.rid == self.parent2.rid
        return parents_same or parents_opposite

petter = Rabbit(2)
hobsy = Rabbit(3)
print(petter)
cotton = Rabbit(1, petter, hobsy)
cotton.set_name('cottontail')
mopsy = petter + hobsy
print(mopsy == cotton) #chould print True cause mopsy has petter and hopsy as parent with the addition above

class Person(object):
    def __init__(self, name):
        #create a person called name
        self.name =  name
        self.birthday = None
        self.lastName = name.split(' ')[-1]
    def setBirthday(self, month, day, year):
        self.birthday = datetime.date(year, month, day)
    def getAge(self):
        if self.bithday == None:
            raise ValueError
        return (datetime.date.today() - self.birthday).days    
    def __lt__(self, other):
        #return True if self's name is lexicographically less than other's name, and false otherwise
        if self.lastName == other.lastName:
            return self.name < other.name
        return self.lastName < other.lastName
"""
"""
class dic(object):
    def tryD(self, shift):
        lower='abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz'
        upper='ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ'
        #lo=string.ascii_lowercase
        #up=string.ascii_uppercase
        print(lower)
        print(upper)
        self.lowerCaseDict = {}
        shift = 26
        #upperCaseDict = {}
        #l = 0
        for i in range (shift):
            self.lowerCaseDict[lower[i]]=lower[i+3]
            self.lowerCaseDict[upper[i]]=upper[i+3]
        return self.lowerCaseDict

f ={'a': 'a', 'b': 'b', 'c': 'c', 'd': 'd', 'e': 'e', 'f': 'f', 'g': 'g', 'h': 'h', 'i': 'i', 'j': 'j', 'k': 'k', 'l': 'l', 'm': 'm', 'n': 'n', 'o': 'o', 'p': 'p', 'q': 'q', 'r': 'r', 's': 's', 't': 't', 'u': 'u', 'v': 'v', 'w': 'w', 'x': 'x', 'y': 'y', 'z': 'z'}   
shif = len(string.ascii_lowercase)
print(dic.tryD(f, shif))
#print(len(lowerCaseDict))
#print(upperCaseDict)

print(shif)
"""
def build_shift_dict(self, shift):
        '''
        Creates a dictionary that can be used to apply a cipher to a letter.
        The dictionary maps every uppercase and lowercase letter to a
        character shifted down the alphabet by the input shift. The dictionary
        should have 52 keys of all the uppercase letters and all the lowercase
        letters only.        
        
        shift (integer): the amount by which to shift every letter of the 
        alphabet. 0 <= shift < 26
        Returns: a dictionary mapping a letter (string) to 
                 another letter (string). 
        '''
        letters = string.ascii_lowercase
        letters_shifted = (letters * 2)[shift : shift + 26]
        letters = letters + letters.upper()
        letters_shifted = letters_shifted + letters_shifted.upper()

        shift_dict = {}

        for i in range(52):
            shift_dict[letters[i]] = letters_shifted[i]
        
        return shift_dict

def apply_shift(self, shift):
        '''
        Applies the Caesar Cipher to self.message_text with the input shift.
        Creates a new string that is self.message_text shifted down the
        alphabet by some number of characters determined by the input shift        
        
        shift (integer): the shift with which to encrypt the message.
        0 <= shift < 26
        Returns: the message text (string) in which every character is shifted
             down the alphabet by the input shift
        '''
        shifted_text = ''
        shift_dict = self.build_shift_dict(shift)

        for char in self.message_text:
            if char in string.ascii_letters:
                char = shift_dict[char]
            shifted_text += char

        return shifted_text





