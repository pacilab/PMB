"""
Example 1
Binomial distribution

Sample random number from binomial distribution.
Compare with distribution function.
Prove that for n -> infinity the binomial tends to Gaussian
"""

# import libraries
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import binom

# define Gaussian distribution
def gaussian(x, m, s):
    return 1 / np.sqrt(2 * np.pi * s**2) * np.exp (- (x-m)**2 / (2*s**2))

# setting the values of n and p
n = 100
p = 0.5

# sample a binomial distribution
sample = np.random.binomial(n, p, 10000)
# plot the histogram
plt.hist(sample, bins = 10, rwidth = 0.8, density = True)

# calculate the "theoretical" binomial distribution
r_values = np.arange(n + 1)
y = [binom.pmf(r, n, p) for r in r_values]
# plot the curve
plt.plot(r_values, y)

# calculate the associated Gaussian function
mean = n*p
std = np.sqrt(n*p*(1-p))
x = np.linspace(0, n, 1000)
y_gauss = gaussian(x, mean, std)
# plot the curve
plt.plot(x, y_gauss)