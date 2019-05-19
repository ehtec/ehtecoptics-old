import numpy as np
import matplotlib.pyplot as plt

n = 1000

radius = np.sqrt(np.arange(n) / float(n))

golden_angle = np.pi * (3 - np.sqrt(5))
theta = golden_angle * np.arange(n)

points = np.zeros((n,2))
points[:,0] = np.cos(theta)
points[:,1] = np.sin(theta)
points *= radius.reshape((n,1))

print points

plt.gca().set_aspect('equal',adjustable='box')

plt.scatter(*zip(*points))

plt.show()
