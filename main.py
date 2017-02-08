# coding: utf-8
import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
import csv
import math
from mpl_toolkits.mplot3d import Axes3D
mpl.rcParams['legend.fontsize'] = 10

f = open('./data.csv', 'r')
reader = csv.reader(f)
header = next(reader)
dimension = []
C = []
gamma = []
accuracy = []

for row in reader:
    dimension.append(int(row[0]))
    C.append(float(row[1]))
    gamma.append(float(row[2]))
    accuracy.append(float(row[3]))

fig = plt.figure()
ax = Axes3D(fig)
ax.set_xlabel("dimension")
ax.set_ylabel("C")
ax.set_zlabel("gamma")
ax.plot(dimension, C, gamma, "o", color="#cccccc", ms=4, mew=0.5)
ax.legend()
plt.show()
