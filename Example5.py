"""
Example 6
Monty Hall problem

Give a numerical solution to the Monty Hall problem
"""

import random
import numpy as np

n = 100000

doors = [0, 1, 0]

win_y = 0
win_n = 0
for i in range(n):
    
    random.shuffle(doors)

    choice = random.choice([0, 1, 2])
    status = doors[choice]
    
    if status == 1:
        win_n += 1
    
    if status == 0:
        win_y += 1

perc_n = win_n/n*100
perc_y = win_y/n*100
print("Win percentage (no change): %5.2f" % perc_n)
print("Win percentage (   change): %5.2f" % perc_y)