"""
Example 3
Monte Carlo

Calculate pi using the Monte Carlo integration method
How many iterations are needed to get 10 significant digits of pi?
"""

# import libraries
import numpy as np

n = 100_000

p_in = 0
for i in range(n):
    x = np.random.random()
    y = np.random.random()
    if x**2 + y**2 < 1:
        p_in += 1

area = p_in / n
pi = 4 * area
diff = np.abs(pi - np.pi)

print("Estimated pi:  %5.10f" % pi)
print("Accuracy:      %5.10f" % diff)