# -*- coding: utf-8 -*-
from __future__ import print_function, division
import math
import numpy as np
import pandas as pd



""" This class represents the implementation of the supervised classification algorithm called Logisitic 
regression. Logistic regression is used to assign observations to a discrete set of classes. The function
at the core of this method is Logisitic function.
----------------------

 Parameters:
        epochs : float
        the number of iterations, this model will tune the weights for

        learn_rate : float
        the step length that will be used to update the weight
        
        X : float
        the weights that this model will be initialized with
        
        y: int
        the actual class that each of these weights belong to
        
        add_intercept: float
        the intercept like y = m(x) + c, where c is the intercept
            
"""
class LogisticRegression(object):
    
    
    def __init__(self, epochs, learn_rate):
        self.epochs = epochs
        self.learn_rate = learn_rate
        
        
        
        
    
    def sigmoid_function(self,values):
        """
        This function calculates the sigmoid function. The output of the sigmoid function is always 
        between 0 and 1.
        
        """
        return 1 / (1 + np.exp(-values))
    
    def weights_initialize(self, num_features):
        """ Initialize weights randomly [-1/N, 1/N] """
        limit = 1 / math.sqrt(num_features)
        self.w = np.random.uniform(-limit, limit, (num_features,))
        
    def predict(self, X):
        
         
            y_pred = np.round(self.sigmoid_function(X.dot(self.w))).astype(int)
            return y_pred    
        
    def fit(self,X,y):
        """
        This function is to be used to tune the weights, essentially training the model on a high
        level.
        
        """
        
        """ Initializing the weights X """
        self.weights_initialize(X.shape[1])
        
        for i in range(self.epochs):
            
            scores = np.dot(X,self.w)
            y_pred = self.sigmoid_function(scores)
            
            
            output_error = y - y_pred
            
            gradient = np.dot(X.T,output_error)
            
            self.w += self.learn_rate*gradient
        
        
     
        