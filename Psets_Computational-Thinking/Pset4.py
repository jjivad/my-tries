# -*- coding: utf-8 -*-
"""
Created on Wed Apr 24 04:02:42 2019

@author: VIJ Global
"""

# problem 1, curve fitting
import numpy as np
import os
os.environ["OPENBLAS_NUM_THREADS"] = "1"

def generate_models(x, y, degs):
    """
    Generate regression models by fitting a polynomial for each degree in degs
    to points (x, y).
    Args:
        x: a list with length N, representing the x-coords of N sample points
        y: a list with length N, representing the y-coords of N sample points
        degs: a list of degrees of the fitting polynomial
    Returns:
        a list of numpy arrays, where each array is a 1-d array of coefficients
        that minimizes the squared error of the fitting polynomial
    """
    # TODO
    return [np.polyfit(x, y, z) for z in degs]

# problem 2, 
import numpy as np
import os
os.environ["OPENBLAS_NUM_THREADS"] = "1"

def r_squared(y, estimated):
    """
    Calculate the R-squared error term.
    Args:
        y: list with length N, representing the y-coords of N sample points
        estimated: a list of values estimated by the regression model
    Returns:
        a float for the R-squared error term
    """
    # TODO
    y, estimated = np.array(y), np.array(estimated)
    SEE = ((estimated - y)**2).sum()
    mMean = y.sum()/float(len(y))
    MV = ((mMean - y)**2).sum()
    return 1 - SEE/MV

# problem 3, 
# Problem 3
y = []
x = INTERVAL_1
for year in INTERVAL_1:
    y.append(raw_data.get_daily_temp('BOSTON', 1, 10, year))
models = generate_models(x, y, [1])
evaluate_models_on_training(x, y, models)

What is the R^2 value? (use 3 decimal places)

0.005 correct
"""

# problem 4,
# 4-1
"""
# Problem 4: FILL IN MISSING CODE TO GENERATE y VALUES
x1 = INTERVAL_1
x2 = INTERVAL_2
y = []
# MISSING LINES
models = generate_models(x1, y, [1])    
evaluate_models_on_training(x1, y, models)

for year in INTERVAL_1:
    y.append(numpy.mean(raw_data.get_yearly_temp('BOSTON', year)))
"""
# 4-2
"""
What is the R^2 value? (use 3 decimal places)

0.085 correct
"""

# problem 5
"""
Which graph, choosing a specific day (Jan 10) or calculating the yearly average, indicates that almost none of the data variation is learned by our model?

choosing a specific day correct

Which graph, choosing a specific day (Jan 10) or calculating the yearly average, supports more the claim that global warming is leading to an increase in temperature?

calculating the yearly average correct
"""