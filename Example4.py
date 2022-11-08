"""
Example 5
Markov chains

Consider a Markov chain with transition matrix

pi = [[1/2, 1/4, 1/4],
      [1/3,   0, 2/3],
      [1/2, 1/2,   0]]

Simulate the trajectory of 1 particle starting from initial state 0.
Simulate the trajectory of N particles starting from random initial states. 
Check that probability distribution tends to the equilibrium state:

solution = [0.457, 0.257, 0.286]
"""

import numpy as np
import matplotlib.pyplot as plt

nparticles = 100
nstep = 10000

initial_state_prob = [1, 0, 0]

pi = [[1/2, 1/4, 1/4],
      [1/3,   0, 2/3],
      [1/2, 1/2,   0]]

solution = [0.457, 0.257, 0.286]

def evolution(state, pi, n):
    
    states = [state]
    
    p1 = pi[state][0]
    p2 = pi[state][1]
    p3 = pi[state][2]
    
    for i in range(n):        
        r = np.random.random()

        if r < p1:
            new_state = 0
        elif r >= p1 and r < p1 + p2:
            new_state = 1
        else:
            new_state = 2
        states.append(new_state)

    return states

final_state = [0, 0, 0]
for i in range(nparticles):    

    initial_state = np.random.choice([0, 1, 2], p = initial_state_prob)
    particle_states = evolution(initial_state, pi, nstep)
    final_state[particle_states[-1]] += 1

norm_final_state = [state / nparticles for state in final_state]

plt.figure()
plt.bar([1, 2, 3], norm_final_state, alpha = 0.8, 
        color='grey', edgecolor='black')
plt.plot([1, 2, 3], solution, 'o', color = 'red')
plt.xticks([1, 2, 3], ["A", "B", "C"])
plt.show()
