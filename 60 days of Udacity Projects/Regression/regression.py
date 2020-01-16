from __future__ import print_function, division
import math
import numpy as np
import pandas as pd

# Implementation of Linear Regression from scratch
class BasicRegression():
    """ This regression model represents the relationship between an independant variable x and dependant variable y.
    ---------

    Parameters:
        epochs : float
        the number of iterations, this model will tune the weights for

        learn_rate : float
        the step length that will be used to update the weights
    """

    def __init__(self, epochs, learn_rate,w):
        self.epochs = epochs
        self.learn_rate = learn_rate
        self.w = w

    def weights_initialize(self, num_features):
        """ Initialize weights randomly [-1/N, 1/N] """
        limit = 1 / math.sqrt(num_features)
        self.w = np.random.uniform(-limit, limit, (num_features,))

    def fit(self, X ,y):
        """ This is the function to train the model"""

        """Inserting constant ones in X"""
        X = np.insert(X,0,1,axis = 1)
        self.weights_initialize(num_features=X.shape[1])
        for i in range(self.epochs):
            y_pred = X.dot(self.w)
            mse = np.mean(0.5 * (y - y_pred)**2)
            grad = -np.dot((y - y_pred), X)
            self.w -= self.learn_rate * grad
            

    def predict(self,X):
        # Insert constant ones for bias weights
        X = np.insert(X, 0, 1, axis=1)
        y_pred = X.dot(self.w)
        return y_pred









