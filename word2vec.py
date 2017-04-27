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

f_status = open('./word2vec_full_vectors/word2vec_100.csv', 'r')
reader_status = csv.reader(f_status)
header_status = next(reader_status)
color_list = []
for row in reader_status:
    if row[1] == 'Accept':
        color_list.append('red')
    else:
        color_list.append('blue')


f = open('./converted_to_3d/converted_3d_100.csv', 'r')
reader = csv.reader(f)
header = next(reader)
dimension = []
X = []
Y = []
Z = []

for row in reader:
    X.append(float(row[0]))
    Y.append(float(row[1]))
    Z.append(float(row[2]))

fig = plt.figure()
ax = Axes3D(fig)
ax.set_xlabel("X")
ax.set_ylabel("Y")
ax.set_zlabel("Z")

for (i, x) in enumerate(X):
    ax.plot([X[i]], [Y[i]], [Z[i]], "o", color=color_list[i], ms=4, mew=0.5)
    # ax.plot([X[i]], [Y[i]], [Z[i]], "o", ms=8, mew=0.5)
ax.legend()

plt.show()
