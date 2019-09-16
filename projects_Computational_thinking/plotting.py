# -*- coding: utf-8 -*-
"""
Created on Sat May  4 17:29:09 2019

@author: VIJ Global
"""

import pylab as plt

mySamples = []
myLinear = []
myQuadratic = []
myCubic = []
myExponential = []

for i in range (0, 30):
    mySamples.append(i)
    myLinear.append(i)
    myQuadratic.append(i**2)
    myCubic.append(i**3)
    myExponential.append(1.5**i)
 
print('Sample = ', mySamples)
print('')
print('Linear = ',myLinear)
print('')
print('Quadratic = ', myQuadratic)
print('')
print('Cubic = ', myCubic)
print('')
print('Exponential = ', myExponential)
print('')
#first trial, all of them display in one chart
print('Samples compare to all the other graph')
plt.figure('All graphs')
plt.title('Linear vs Quadratic vs Cubic vs Exponential')
plt.ylim(0, 50000)
plt.plot(mySamples, myLinear, label = 'linear')
plt.plot(mySamples, myQuadratic, label = 'quadratic')
plt.plot(mySamples, myCubic, label = 'cubic')
plt.plot(mySamples, myExponential, label = 'exponential')
plt.legend(loc = 'upper left')

#second trial, different charts
#put title, rename the axis, color the graph
plt.figure('Linear')
plt.clf() #cleaning windows/figure
plt.title('Linear graph') #title
plt.xlabel('Samples') #rename x 
plt.ylabel('Linear') # rename y
plt.plot(mySamples, myLinear)


plt.figure('Quadratic')
plt.clf()
plt.title('Quadratic graph')
plt.xlabel('Samples')
plt.ylabel('Quadratic')
plt.plot(mySamples, myQuadratic)


plt.figure('Cubic')
plt.clf()
plt.title('Cubic graph')
plt.xlabel('Samples')
plt.ylabel('Cubic')
plt.plot(mySamples, myCubic)


plt.figure('Exponential')
plt.clf()
plt.title('Exponential graph')
plt.xlabel('Samples')
plt.ylabel('Exponential')
plt.plot(mySamples, myExponential)


#naming graphs, comaparing, legends, etc
plt.figure('LinearQuadratic')
plt.clf()
plt.title('Linear vs Quadratic')
plt.ylim(0, 1000) # y limite
plt.plot(mySamples, myLinear, 'r--' ,label = 'linear') # r-- means red color with/in dashes
plt.plot(mySamples, myQuadratic, 'bo', linewidth = 0.5, label = 'quadratic') # bo means blue color with/in circles
plt.legend(loc = 'upper left')

plt.figure('QuadraticCubic')
plt.clf()
plt.title('Cubic vs Quadratic')
plt.ylim(0, 10000)
plt.plot(mySamples, myCubic, linewidth = 2.0, label = 'cubic')
plt.plot(mySamples, myQuadratic, label = 'quadratic')
plt.legend(loc = 'upper left')

plt.figure('CubicExponential2')
plt.clf()
plt.title('Cubic vs Exponential')
plt.ylim(0, 40000)
plt.plot(mySamples, myCubic, 'g^', linewidth = 2.0, label = 'cubic') # g^ means in green color with/in triangles
plt.plot(mySamples, myExponential, label = 'exponential' )
plt.legend(loc = 'upper left') # put it after the plot so that it can pick the graph cplors and names


#subplotting
plt.figure('QuadraticCubic2')
plt.clf()
plt.title('Cubic vs Quadratic subplot row')
plt.subplot(211) #this one is to have sub graph/plot in the same tricks, same (titles) -> first number is the row, 2nd is the column, and last the position
plt.ylim(0, 10000) # 2 rows 1 column first position (so that the other graph can take the second postion)
plt.plot(mySamples, myCubic, linewidth = 5.0, label = 'cubic') # linewidth is for the size of the graph line
plt.legend(loc = 'upper left')
plt.subplot(212) # 2 rows 1 column and second position
plt.ylim(0, 10000)
plt.plot(mySamples, myQuadratic, 'r-', label = 'quadratic') # a single dash is a line for the shape
plt.legend(loc = 'upper left')

plt.figure('Quad')
plt.clf()
plt.title('subplot column')
plt.subplot(121)
plt.ylim(0, 10000)
plt.plot(mySamples, myCubic, linewidth = 2.0, label = 'cub')
plt.legend(loc = 'upper left')
plt.subplot(122)
plt.ylim(0, 10000)
plt.plot(mySamples, myQuadratic, 'r--', label = 'quad')
plt.legend(loc = 'upper left')



#log scale (changing the scale)
plt.figure('QuadraticCubic3')
plt.figure('CubicExponential3')
plt.clf()
plt.title('Cubic vs Exponential log scale')
#plt.ylim(0, 40000)
plt.plot(mySamples, myCubic, 'g^', linewidth = 2.0, label = 'cubic') # g^ means in green color with/in triangles
plt.yscale('log')
plt.plot(mySamples, myExponential, label = 'exponential' )
plt.legend(loc = 'upper left')












