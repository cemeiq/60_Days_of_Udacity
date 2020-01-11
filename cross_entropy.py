# -*- coding: utf-8 -*-
"""
Created on Sat Jan 11 19:34:42 2020
 Python Script for calculating Cross Entropy given two lists Y and P
@author: iqra1
"""

import numpy as np

# Write a function that takes as input two lists Y, P,
# and returns the float corresponding to their cross-entropy.
def cross_entropy(Y, P):
    sum = 0
    for i, j in zip(Y,P):
        sum += np.multiply(i,np.log(j)) + np.multiply((1-i),np.log(1-j))
    
    return -sum