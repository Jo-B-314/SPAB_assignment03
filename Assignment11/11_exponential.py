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
from tqdm import tqdm

random.seed(42)

def exponential(n, T, x):
    r1_array = []
    r2_array = []
    
    
    for beta in tqdm(x):
        d1_array = []
        d2_array = []
        l1_array = []
        l2_array = []
        
        for i in range(0,T):
            data = np.random.exponential(beta, size=n)
            mean_ = np.mean(data)
            median_ = np.median(data)
            delta_1 = 1/mean_
            d1_array.append(delta_1)
            delta_2 = np.log(2) / median_
            d2_array.append(delta_2)
            #absolute loss
            loss_1 = abs(beta-delta_1)
            l1_array.append(loss_1)
            loss_2 = abs(beta-delta_2)
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
x = np.arange(0.01, 100.0, 0.01)
exponential(n, T, x)

