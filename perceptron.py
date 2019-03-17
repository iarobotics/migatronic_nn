#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import numpy as np

class Perceptron(object):
    def __init__(self, input_size, epochs=100):
        # initialize variables
        self.weight = np.zeros(input_size)
        self.bias = np.zeros(1)
        self.epochs = epochs

    @staticmethod
    def activation_fn(z):
        # step function: z >=0: return 1 else return 0
        if z >= 0:
            return 1.
        else:
            return 0.

    def predict(self, X):
        # forward propagation
        z = self.weight.T.dot(X) + self.bias
        a = self.activation_fn(z)
        return a

    def fit(self, X, y):
        # train our weight and bias
        for _ in range(self.epochs):
            for i in range(y.shape[0]):
                # full forward pass
                a = self.predict(X[i])
                # compute the error
                error = y[i] - a
                # update the weight and bias
                self.weight = self.weight + error * X[i]
                self.bias = self.bias + error

if __name__ == '__main__':
    X = np.array([
        [0, 0],
        [0, 1],
        [1, 0],
        [1, 1]
    ])
    y = np.array([0, 0, 0, 1])

    perceptron = Perceptron(input_size=2)
    perceptron.fit(X, y)

    accuracy = 0.
    for i in range(y.shape[0]):
        accuracy += perceptron.predict(X[i]) == y[i]
    accuracy = accuracy / y.shape[0]

    print("Accuracy: {:.4}".format(accuracy))

    print("Weight: {}".format(perceptron.weight))
    print("Bias: {}".format(perceptron.bias))
