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
        if(np.size(newarray) == 0):
            print("Array is empty")
            continue
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
                print("Line not valid")
                break
                
        print("-----------------")
        print("Original Array", line)
        if(isValid):
            convarray = newarray.astype(float)
            print("Float Array:", convarray)
                
            log_add(convarray)
        else:
            print("ERROR - FALSE INPUT")
    fobj.close()

def log_add(array: np.array) -> np.array:
    addition = 0
    prime_max = np.nanmax(array)
    print("max of array:", prime_max)
    
    max_value = math.exp(prime_max)
    print("exp(max of array):", max_value)
    if(max_value == 0):
        print("Max Value is 0, so Addition is 0.")
        return
    # return if array is empty
    if(np.size(array) == 0):
        print("Array is empty")
        return
    
    y = np.size(array)-1
    addition = max_value
    
    for i in range(0,y):
        addition += array[i] / max_value
        ##print(addition)
    print("Addition r:", addition)


read_commandline()
