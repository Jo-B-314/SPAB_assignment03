# -*- coding: utf-8 -*-
"""
Created on Tue Dec  7 15:55:08 2021

@author: chris
"""
import math
import random
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import chi2
from scipy.stats import rv_continuous

from itertools import product

# SORRY this is not working as it should

alphabet = [
    'A',
    'C',
    'G',
    'T']


def convert(s):
    strin = "" 
    for x in s:
        strin += x 
    return strin

"""
N = number of repeats
"""

def motif(n,k,N):
    l = n+k-1
    pA = pT = pC = pG = 1/4
    probs = [pA, pC, pG, pT]
    a = int(math.pow(4,k))
    
    # array of N lists, each list index counter for k_tuple
    nmotifs = np.zeros(N, dtype=list)
    delta = np.zeros(a, dtype=int)
    delta_pdf = np.zeros(a, dtype=int)
    empty = np.zeros(a, dtype=np.uint32)
    for i in range(N):
        nmotifs[i] = empty
        
    # k-tuples
    comb = product(alphabet, repeat=k)
    k_tuples_list = list(comb)
    k_tuples_strings = np.zeros(a, dtype='object')
    for i in range(a):
        stri = []
        for j in range(k):
            stri.append(k_tuples_list[i].__getitem__(j))
        string = convert(stri)
        k_tuples_strings[i] = string
    
    # count
    for i in range(N):
        # N-times construct DNA, search for k-tuples
        genome = "".join(random.choices(alphabet, probs, k=l))
        for j in range(a):
            nmotifs[i][j] = genome.count(k_tuples_strings[j])
     
        
    # delta = sum (observed-expected)^2/expected
    expected = n/a
    
    for j in range(a):
        sum = 0
        for i in range(N) :
            x = math.pow(nmotifs[i][j]-expected, 2) / expected
            sum += x
        delta[j] = sum
    d_sum = 0
    for j in range(a):
        d_sum += delta[j]
        
    mean = d_sum // a
    sigma = 0
    for l in delta :
        sigma += (l-mean)**2
    sigma = math.sqrt(sigma/a)
    for i in range(a):
        delta_pdf[i] = (1.0 / (sigma * math.sqrt(2*math.pi))) * math.exp(-0.5*math.pow(((delta[i]-mean)/sigma),2))
    
    # chi square, source geeksforgeeks
    numargs = chi2.numargs
    [a] = [1] * numargs
    rv = chi2(a)
    
    distribution = np.linspace(0, np.minimum(rv.dist.b, 1))
  
    plot = plt.plot(distribution, rv.pdf(distribution))
  
        
motif(1000000, 8, 100)