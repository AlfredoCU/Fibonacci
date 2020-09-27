#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 22 19:28:22 2020

@author: alfredocu
"""

import numpy as np


# Exponentiation by squaring
def expBySquaring(n, exp):
    if exp == 1:
        return n
    elif exp % 2 == 0:
        return expBySquaring(np.dot(n, n), exp / 2)
    else:
        return np.dot(n, expBySquaring(np.dot(n, n), (exp - 1) / 2))  # is odd


# Fibonacci
def fibonacci(n=10):
    matrix = np.array([[1, 1], [1, 0]], dtype=object)
    if n <= 1:
        return matrix[0][0]
    else:
        result = expBySquaring(matrix, n)  # n - 1
        return result[0][0]


print(fibonacci())
