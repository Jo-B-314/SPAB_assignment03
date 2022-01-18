# -*- coding: utf-8 -*-
"""
Created on Sun Jan 16 11:43:32 2022

@author: lisar
"""
import numpy as np
import math
import random
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from scipy import stats
from tqdm import tqdm

random.seed(42)

def normal(n, T, x):
    r1_array = []
    r2_array = []
    
    
    for sigma in tqdm(x):
        d1_array = []
        d2_array = []
        l1_array = []
        l2_array = []
        
        for i in range(0,T):
            data = np.random.normal(sigma, size=n)
            mean_ = np.mean(data)
            median_ = np.median(data)
            # DELTA 1
            var_sum = 0
            for j in data:
                var_sum += pow(j-mean_,2) 
            delta_1 = (1/(n-1)) * var_sum
            d1_array.append(delta_1)
            # DELTA 2
            iqr_ = stats.iqr(data, interpolation = 'midpoint')
            delta_2 = pow(( iqr_/ 1.349) , 2)
            d2_array.append(delta_2)
            #absolute loss
            loss_1 = abs(sigma-delta_1)
            l1_array.append(loss_1)
            loss_2 = abs(sigma-delta_2)
            l2_array.append(loss_2)
            #print(beta, i+1, 1/mean_, np.log(2) /median_, loss_1, loss_2)
    
        # Risk is calculated per T
        loss1_sum = np.sum(l1_array)
        loss2_sum = np.sum(l2_array)
        
        #avg loss
        R1 = 1/T * loss1_sum
        R2 = 1/T * loss2_sum
        
        r1_array.append(R1)
        r2_array.append(R2)
    
    plotting(x, r1_array, r2_array, "Exponential Estimators")
    
def plotting(x, R1, R2, title):
    
    #print(R1)
    #print(R2)
    
    #fig = plt.figure()
    fig, (ax1, ax2) = plt.subplots(1,2, figsize=(12,6))
    
    #ax = fig.add_axes([1,1,1,1])
    
    ax1.plot(x, R1 , label='Delta-1', color='b')
    ax2.plot(x, R2, label= 'Delta-2', color='r')
    
    fig.legend(loc='center right')

    ax1.set_title(title)
    ax1.set_ylabel("approx. risk")
    ax1.set_xlabel("parameter value")
    ax2.set_title(title)
    ax2.set_ylabel("approx. risk")
    ax2.set_xlabel("parameter value")
    plt.show()
    plt.savefig('figure.png')

# Exponential
n = 21
T = 1000
x = np.arange(0.1, 10.0, 0.1)
normal(n, T, x)

