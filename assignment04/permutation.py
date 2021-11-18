# -*- coding: utf-8 -*-
"""
Created on Thu Nov 18 15:32:14 2021

@author: lisar
"""

import random
import numpy as np
        
# hit == permutation without fixpoint
hit_counter = 0
a = list(range(0,100+1))
n = len(a)
fixpoint_counter = 0
    
while(hit_counter < 1000000):
    fixpoint_flag = False
    pa = np.random.permutation(100)

# check my array for fixpoints
    for i in range(0,100):
        if(pa[i] == i):
            #print("found fixpoint at index", i)
            fixpoint_counter += 1
            fixpoint_flag = True
            break
    if(fixpoint_flag == False):
        hit_counter += 1
        print(hit_counter)
    
print("Total amount of permutations: " , hit_counter+fixpoint_counter)

# needed amount is 2718015
