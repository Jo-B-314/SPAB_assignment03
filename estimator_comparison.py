from numpy.random import seed

from numpy.random import normal

import numpy as np

from scipy.stats import iqr

import matplotlib.pyplot as plt



# =============================================================================
# The two estimators perform quite differently. In comparison to each other 
# delta 2 always tend to be a bit more on the left side. Delta 1 tends to be a
# bit more centered. With the growing n, the estimators get closer to the middle
# and in the case n = 1000 there is barely a difference left. So what we see is
# that estimators get closer to the real value (1 in this case) the bigger the 
# sample size is. An explanation can be, that when there are more samples, 
# outliers do not have as much of an effect as with small sample sizes.
# =============================================================================


#seed(42)

def process(n):
    list1 = []
    list2 = []
    for i in range(1000):
        # generate n samples
        data = normal(loc=0.0, scale=1, size=n)
        # inter quartile range of n samples
        iqr_data = iqr(data)
        d_2 = (iqr_data/1.349)**2
        list2.append(d_2)
        d_2 = 0
        # mean of 10 samples
        mean_data = np.mean(data)
        d_1 = 1/(n-1) * n * np.var(data)
        list1.append(d_1)
        d_1 = 0

    print("______________")
    print("n = ", n)
    plt.hist(list1)
    plt.title("Delta 1")
    plt.xlabel('Delta')
    plt.show()
    
    plt.hist(list2)
    plt.title("Delta 2")
    plt.xlabel('Delta')
    plt.show()



process(10)
process(100)
process(1000)