# coding: utf-8
import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
import csv
import math
from mpl_toolkits.mplot3d import Axes3D
mpl.rcParams['legend.fontsize'] = 10

import matplotlib.cm as cm

f_status = open('./word2vec_full_vectors/word2vec_100.csv', 'r')
reader_status = csv.reader(f_status)
header_status = next(reader_status)
color_list = []
for row in reader_status:
    if row[1] == 'Accept':
        color_list.append('blue')
    else:
        color_list.append('red')


f = open('./converted_to_3d/converted_3d_80.csv', 'r')
reader = csv.reader(f)
header = next(reader)
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
ax.legend()

plt.show()
