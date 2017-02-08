# coding: utf-8
import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
import csv
import math
from mpl_toolkits.mplot3d import Axes3D
mpl.rcParams['legend.fontsize'] = 10

import matplotlib.cm as cm

def colorscale(v):
    t = math.cos(4 * math.pi * v)
    c = int(((-t / 2) + 0.5) * 255)
    if v >= 1.0:
        return '#%02X%02X%02X' % (255, 0, 0)
    elif v >= 0.75:
        return '#%02X%02X%02X' % (255, c, 0.0)
    elif v >= 0.5:
        return '#%02X%02X%02X' % (c, 255, 0)
    elif v >= 0.25:
        return '#%02X%02X%02X' % (0, 255, c)
    elif v >= 0:
        return '#%02X%02X%02X' % (0, c, 255)
    else:
        return '#%02X%02X%02X' % (0, 0, 255)

def colorscale2(v):
    if v >= 0.6:
        return 'red'
    elif v < 0.6 and v >= 0.55:
        return 'hotpink'
    elif v < 0.55 and v >= 0.5:
        return 'green'
    elif v < 0.5 and v >= 0.4:
        return 'blue'
    elif v >= 0:
        return 'gray'
    else:
        return 'black'

f = open('./data.csv', 'r')
reader = csv.reader(f)
header = next(reader)
dimension = []
C = []
gamma = []
accuracy = []
colorlist = []

for row in reader:
    dimension.append(int(row[0]))
    C.append(float(row[1]))
    gamma.append(float(row[2]))
    accuracy.append(float(row[3]))
    colorlist.append(colorscale2(float(row[3])))

fig = plt.figure()
ax = Axes3D(fig)
ax.set_xlabel("dimension")
ax.set_ylabel("C")
ax.set_zlabel("gamma")

for (i, x) in enumerate(dimension):
    ax.plot([dimension[i]], [C[i]], [gamma[i]], "o", color=colorlist[i], ms=4, mew=0.5)
ax.legend()
plt.show()
