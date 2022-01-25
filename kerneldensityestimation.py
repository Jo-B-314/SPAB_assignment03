# -*- coding: utf-8 -*-
"""
Created on Tue Jan 25 12:14:33 2022

@author: lisar
"""


# Sources
# https://github.com/scikit-learn/scikit-learn/blob/main/sklearn/neighbors/_kde.py
# https://stackabuse.com/kernel-density-estimation-in-python-using-scikit-learn/
# https://scikit-learn.org/stable/auto_examples/neighbors/plot_kde_1d.html
# https://het.as.utexas.edu/HET/Software/Scipy/generated/scipy.stats.gaussian_kde.html
# https://github.com/scipy/scipy/issues/6176

import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm
from sklearn.neighbors import KernelDensity

# =============================================================================
# General K(x)
# mean and median at x = 0
# support R or [-b, b] for some b > 0
# shifting and scaling: Kh(x) = K((x-xi)/h)/h
# -> for centereing around one of the sample points
# -> scaling for bandwidth h
# 
# Espanechikov: K(x) 1-x^2 for |x|<= 1
# 
# h = 1/2
# n = 50
# =============================================================================

N = 50
h = 0.5
X =[[-3.4], [-3.21], [-2.47], [-2.45], [-2.44], [-1.9], [-1.72],
                [-1.65], [-1.43],[-1.03], [-0.97], [-0.61], [-0.59], [-0.05],
                [0.39], [0.42], [0.42], [0.47], [0.47],[0.52], [0.58], [0.66],
                [0.69], [0.71], [0.78], [0.84], [0.88], [0.91], [1.0], [1.0],
                [1.02], [1.09], [1.14], [1.23], [1.27], [1.27], [1.29], [1.3],
                [1.31], [1.35], [1.4], [1.45], [1.47], [1.54], [1.66], [1.81],
                [1.83], [1.86], [2.22], [2.87]]

X_plot = np.linspace(-5, 10, 1000)[:, np.newaxis]

true_dens = 0.25 * norm(-2, 1).pdf(X_plot[:, 0]) + 0.25 * norm(0, 1).pdf(X_plot[:, 0]) + 0.5 * norm(1.1, 2).pdf(X_plot[:, 0])

fig, ax = plt.subplots()
ax.fill(X_plot[:, 0], true_dens, fc="black", alpha=0.2, label="input distribution")
lw = 2


kde = KernelDensity(kernel='epanechnikov', bandwidth=h).fit(X)
log_dens = kde.score_samples(X_plot)
ax.plot(
    X_plot[:, 0],
    np.exp(log_dens),
    color='navy',
    lw=lw,
    linestyle="-",
    label="kernel = '{0}'".format('epanechnikov'),
   )

ax.text(6, 0.38, "N={0} points".format(N))

ax.legend(loc="upper right")

ax.set_xlim(-5, 6)
ax.set_ylim(-0.02, 0.6)
plt.show()

#----------------------------------------------------------- BONUS
# For Cross Validation we use the sklearn function GridSearchCrossValidation.
# It takes different bandwith parameters and returns the maximized log-
# likelihood of data

from sklearn.model_selection import GridSearchCV

h = np.arange(0.05,2,0.05)

fig, ax = plt.subplots(nrows=2, ncols=3, figsize=(10, 7))
plt_ind = np.arange(6) + 231

for b, ind in zip(h, plt_ind):
    kde_model = KernelDensity(kernel='epanechnikov', bandwidth=b)
    kde_model.fit(X)
    score = kde_model.score_samples(X_plot)
    plt.subplot(ind)
    plt.fill(X_plot, np.exp(score), c='green')
    plt.title("h="+str(b))

fig.subplots_adjust(hspace=0.5, wspace=.3)
fig.suptitle("Effect of bandwidth on Estimation")
plt.show()


kde = KernelDensity(kernel='epanechnikov').fit(X)
grid = GridSearchCV(kde,{'bandwidth': h})
grid.fit(X)
kde = grid.best_estimator_
log_dens = kde.score_samples(X)
plt.fill(X, np.exp(log_dens), c='green')
plt.title('Optimal estimate with Epanechnikov kernel')
plt.show()
print("optimal bandwidth: " + "{:.2f}".format(kde.bandwidth))



