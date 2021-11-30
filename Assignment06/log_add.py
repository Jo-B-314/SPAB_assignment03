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
  
def log_add(array: np.array) -> np.array:
    addition = 0
    size = np.size(array)
    log_array = math.log(array)
    print(array)
    print(log_array)
        # add i on i+1 and safe 
        #addition += p1 + log(1+(np.exp(q1-p1)))     
    return 0


read_commandline()
