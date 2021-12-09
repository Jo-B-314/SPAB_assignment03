# -*- coding: utf-8 -*-
"""
Created on Tue Dec  7 15:55:08 2021

@author: chris
"""
import math
import random
import numpy as np

from itertools import product

motif1 = 'ATCTGGAC'
motif2 = 'ACACACAC'

alphabet = [
    'A',
    'C',
    'G',
    'T']

"""
g = G/C content
l = length of genome
n = number of repeats

"""
def convert(s):
  
    # initialization of string to ""
    new = ""
  
    # traverse in the string 
    for x in s:
        new += x 
  
    # return string 
    return new

def motif(n,k,N):
    l = n+k-1
    pA = pT = pC = pG = 1/4
    probs = [pA, pC, pG, pT]
    a = int(math.pow(4,k))
    
    # array of N lists, each list index counter for k_tuple
    nmotifs = np.zeros(N, dtype=list)
    empty = np.zeros(a, dtype=np.uint32)
    for i in range(N):
        nmotifs[i] = empty
        
    #k-tuples
    comb = product(alphabet, repeat=k)
    k_tuples_list = list(comb)
    
    k_tuples_strings = np.zeros(a, dtype='object')
    for i in range(a):
        stri = []
        for j in range(k):
            stri.append(k_tuples_list[i].__getitem__(j))
        string = convert(stri)
        k_tuples_strings[i] = string
    
    for i in range(N):
        # N-mal dna sequenz erstellen und nach k-tuepln suchen
        genome = "".join(random.choices(alphabet, probs, k=l))
        for j in range(a):
            nmotifs[i][j] = genome.count(k_tuples_strings[j])
        #nmotif1[i] = genome.count(motif1)
        #nmotif2[i] = genome.count(motif2)
  
        
motif(100, 2, 5)