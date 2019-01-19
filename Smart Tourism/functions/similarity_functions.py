
import sys
import numpy as np
import pandas as pd
import math


def mod_value(vect):
    # this returns modulus  of vector ......
    l = len(vect)
    s = 0
    for i in range(l):
        s += vect[i]**2
        
    s = math.sqrt(s)
    return s

def cosine_similarity(vect_a,vect_b):

    # returns the cosine similarity of two given vectors ....
    l_a = len(vect_a)
    l_b = len(vect_b)

    if l_a != l_b:
        print("Invalid Arguments")
        return
        
    dot_product = np.dot(vect_a,vect_b)
    mod_a = mod_value(vect_a)
    mod_b = mod_value(vect_b)
    ret_value = dot_product / np.multiply(mod_a,mod_b)
    return ret_value

def covariance(vect_a,vect_b):
    # returns the covariance value between any two vectors ......
    l_a = len(vect_a)
    l_b = len(vect_b)

    if l_a != l_b:
        print("Invalid Arguments")
        return

    a_mean = a.mean()
    b_mean = b.mean()
    value = 0

    for i in range(l_a):
        value += (a[i] - a_mean) * (b[i] - b_mean)

    value = value / l_a

    return value 

def correlation_similarity(vect_a,vect_b):
    # this function returns the pearson's r ratio ......

    std_a = vect_a.std()
    std_b = vect_b.std()
    cov = covariance(vect_a,vect_b)

    value = cov/ (std_b * std_a)
    return value
    pass


