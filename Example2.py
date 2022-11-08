"""
Example 2
Rolling a die

Simulate N rolls of a die.
Show the evolution of the histogram of extracted values at each roll. 
Check that for N -> infinity the probability of finding each face is 1/6.
Simulate an unfair die.
"""

# import libraries
import matplotlib.pyplot as plt
import numpy as np

# number of rolls
n = 600

# define the faces of the die and the list containing the results
die = [1, 2, 3, 4, 5, 6]
res = [0] * len(die)

plt.figure()

for i in range(n):
    plt.clf()
    
    roll = np.random.choice(die)
    res[roll - 1] += 1

    plt.bar(die, res, color = 'orange', edgecolor = 'black')
    
    plt.xlim(0, 7)
    plt.ylim(0, n/2)
    
    plt.pause(0.05)

plt.hlines(n/6, 0, 7, color = 'red', linestyles = '--')