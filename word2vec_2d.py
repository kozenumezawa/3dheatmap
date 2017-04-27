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
id_list =[]
for row in reader_status:
    id_list.append(row[0])
    if row[1] == 'Accept':
        color_list.append('blue')
    else:
        color_list.append('red')


f = open('./converted_to_2d/converted_2d_80.csv', 'r')
reader = csv.reader(f)
header = next(reader)
X = []
Y = []
for (i, row) in enumerate(reader):
    x = float(row[0])
    y = float(row[1])
    if x > 26.5 and y > -10 and y < 0:
        print i + 1, id_list[i], x, y
        X.append(x)
        Y.append(y)

fig = plt.figure()
ax = Axes3D(fig)
ax.set_xlabel("X")
ax.set_ylabel("Y")

for (i, x) in enumerate(X):
    ax.plot([X[i]], [Y[i]], "o", color=color_list[i], ms=4, mew=0.5)
ax.legend()

plt.show()
