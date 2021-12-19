import numpy as np
from matplotlib import pyplot as plt

from scipy.stats import cauchy


def avg_cauchy(n=1000):
    X = np.random.standard_cauchy(n)
    avg = np.mean(X)
    return avg

# X = np.random.standard_cauchy(1000)
# truncate distribution for plotting
# X = X[(X > -25) & (X < 25)]


X_avg = []
for i in range(1000):
    avg = avg_cauchy()
    X_avg.append(avg)

cdf = cauchy.cdf(X_avg)
cdf = sorted(cdf)
plt.plot(cdf)
plt.title("CDF of X_avg")

plt.savefig("cdfOfXavg.png")

cdf = cauchy.cdf(np.arange(0, 10, 0.01))
plt.plot(cdf)
plt.title("CDF of X")
plt.savefig("cdfOfX.png")
