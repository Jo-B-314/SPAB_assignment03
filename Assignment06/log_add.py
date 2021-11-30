# -*- coding: utf-8 -*-
"""
Created on Tue Nov 30 08:47:44 2021

@author: lisar
"""

import math
import sys
import numpy as np


def read_commandline():
    convarray = np.empty(0)
    fobj = open(sys.argv[1], 'r')
    for line in fobj:
        isValid = True
        iniarray = line.split()
        newarray = np.array(iniarray)
        for x in newarray:
            print(x)
            test = x
            test = test.replace('.', '', 1)
            test = test.replace('-','',2)
            test = test.replace('+','',1)
            test = test.replace('inf', '1',1)
            test = test.replace('nan', '1', 1)
            test = test.replace('e', '1',1)
            if not test.isdigit():           
                isValid = False
                print("Line not valid.")
            
        if(isValid):
            convarray = newarray.astype(float)
            log_add(convarray)
        print(convarray)
        
        


  
def log_add(array):
# =============================================================================
#     
#     log_result = 0
#     for i in range(array.size()):
#         p = array[i]
#         q = array[i+1]
#      ## Default is e, i like that
#         p1 = math.log(p)
#         q1 = math.log(q)
#         r = p*q
#         r1 = math.log(r)
#     i+=1
#     return log_result
# =============================================================================
 

read_commandline()
