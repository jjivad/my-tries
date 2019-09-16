# -*- coding: utf-8 -*-
"""
Created on Mon May 27 12:25:29 2019

@author: VIJ Global
"""

import random
        
class Lecture(object):
    def __init__(self, listen, sleep, fb):
        self.listen = listen
        self.sleep = sleep
        self.fb = fb
    def get_listen_prob(self):
        return self.listen
    def get_sleep_prob(self):
        return self.sleep
    def get_fb_prob(self):
        return self.fb
     
def get_mean_and_std(X):
    mean = sum(X)/float(len(X))
    tot = 0.0
    for x in X:
        tot += (x - mean)**2
    std = (tot/len(X))**0.5
    
    cv = std/mean
    return mean, std, cv
        
def lecture_activities(N, aLecture):
    '''
    N: integer, number of trials to run
    aLecture: Lecture object
 
    Runs a Monte Carlo simulation N times.
    Returns: a tuple, (float, float)
             Where the first float represents the mean number of lectures it takes 
             to have a lecture in which all 3 activities take place,
             And the second float represents the total width of the 95% confidence 
             interval around that mean.
    '''
    # IMPLEMENT THIS FUNCTION
    
    l = []
    x = Lecture.get_sleep_prob(aLecture)
    y = Lecture.get_listen_prob(aLecture)
    z = Lecture.get_fb_prob(aLecture)
    item = (x, y, z)
    for i in range (N):        
        l.append(random.choice(item))
        print(l)
    return get_mean_and_std(l)
    
    #choice = get_mean_and_std(aLecture)
#    chos = []
#    for i in range (N):
#        chos.append(random.choice(aLecture))
#    return get_mean_and_std(chos)
    #myList = []
#    for i in range (N):
#        return get_mean_and_std(aLecture)
        #myList.append(random.choice(aLecture))
#        myList = random.choice(aLecture)
#    return get_mean_and_std(myList)
    
    

          
#sample test cases 
#a = Lecture(1, 1, 1)
#print(lecture_activities(100, a))
#the above test should print out (1.0, 0.0)
          
#b = Lecture(1, 1, 0.5)
#print(lecture_activities(4, b))
#the above test should print out something reasonably close to (2.0, 5.516)

#b = Lecture(0.5, 0.5, 0.5)
#print(lecture_activities(3, b))

#d = (1, 1, 0.5)
#print(get_mean_and_std(d))
#
#n = 10
#
#l = []
#for i in range(1000):
#    l.append(random.choice(d))
##print(l)
#print(get_mean_and_std(l))



#n = 5
#a = Lecture(1, 1, 0.5)
#l = []
#x = Lecture.get_sleep_prob(a)
#y = Lecture.get_listen_prob(a)
#z = Lecture.get_fb_prob(a)
#item = (x, y, z)
#for i in range (n):        
#    l.append(random.choice(item))
#    print(l)
#print (get_mean_and_std(l))


#m = [10, 4, 12, 15, 20, 5]
#m = [1, 2, 3] #0.408
#m = [11, 12, 13] #0.068
m = [0.1, 0.1, 0.1] #1.387

print(get_mean_and_std(m))
#l = 5.5377492419453835/11.0
#print(l)








