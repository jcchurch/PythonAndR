#!/usr/bin/env python

import numpy as np
import matplotlib.pyplot as plt

# Simple Linear Regression using the least squares approach.
def linreg(X, Y):
    assert len(X)==len(Y)
    n = len(X)
    EX = sum(X)
    EY = sum(Y)
    EX2 = sum([x*x for x in X])
    EXY = sum([ X[i] * Y[i] for i in range(n)])
    m = (n*EXY - EX*EY) / (n*EX2 - EX*EX)
    b = (EY - m*EX) / n
    return (m, b)

# Read the data of AAPL and MSFT
# [ax, ay, bx, by, cx, cy, dx, dy] = np.loadtxt("quartet.csv", delimiter=' ')
A = np.loadtxt("quartet.csv", delimiter=' ')

ax = A[:, 0]
ay = A[:, 1]
bx = A[:, 2]
by = A[:, 3]
cx = A[:, 4]
cy = A[:, 5]
dx = A[:, 6]
dy = A[:, 7]

print linreg(ax, ay)
print linreg(bx, by)
print linreg(cx, cy)
print linreg(dx, dy)

(m, b) = linreg(ax, ay)
X = np.linspace(0., 15., 100)
Y = X*m + b

plt.plot(X, Y, 'b-')
plt.plot(ax, ay, 'r+')
plt.show()

plt.plot(X, Y, 'b-')
plt.plot(bx, by, 'r+')
plt.show()

plt.plot(X, Y, 'b-')
plt.plot(cx, cy, 'r+')
plt.show()

plt.plot(X, Y, 'b-')
plt.plot(dx, dy, 'r+')
plt.show()
