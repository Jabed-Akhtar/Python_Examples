# -*- coding: utf-8 -*-
"""
Created on Thu Dec 21 16:34:22 2023

@author: jabed
"""

# Imports
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import minimize
from scipy.optimize import minimize_scalar

#%% Data points
# Objective function to minimize
def objective_function(x):
    return (x - 2) ** 2 + (x - 3) ** 2

# Plot the contour of the objective function
x_range = np.linspace(-1, 4, 100)
y_values = [objective_function(x) for x in x_range]

fig, ax = plt.subplots(figsize=(8,5), dpi=80)
ax.plot(x_range, y_values, 'go', label='X and Y Data')
ax.set_title('Input Data')
ax.legend()

# Define a callback function to collect the optimization history
history = []
def callback_function(x):
    history.append(x)

# Perform the minimization with callback
result = minimize(objective_function, 0, method='BFGS', callback=callback_function, options={'disp': True})

# Display the result
print("Optimal parameters:", result.x)
print("Optimal function value:", result.fun)

y_history = []
for x in history:
    y_history.append(objective_function(x))
# Plot the optimal point on the original plot
ax.scatter(history, y_history, color='red', marker='x', s=100, label='Optimal Point')

ax.legend()
