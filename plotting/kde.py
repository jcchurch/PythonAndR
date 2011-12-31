import sys
import math
import matplotlib.pyplot as plt

SQRT_2PI = math.sqrt(2.0 * math.pi)

def gaussian(x):
    return math.exp(-0.5*x*x)/SQRT_2PI

def function_kde(x, y, h, binpoints):
    bins = [0] * len(binpoints)
    for i in range(len(binpoints)):
        bins[i] = y * gaussian( (binpoints[i] - x) / float(h) ) / float(h)

    return bins

if __name__=='__main__':

    x = []
    y = []

    for line in file('presidential_days_in_office.txt'):
        line = line.strip()
        [order, name, daysInOffice] = line.split("\t")
        x.append( float(order) )
        y.append( float(daysInOffice) )

    n = len(x)
    low = min(x)
    high = max(x)
    nbins = n * 1 

    binpoints = [0] * nbins
    masterbin = [0] * nbins

    delta = (high - low) / (nbins - 1)

    b = low
    i = 0
    while b <= high:
        binpoints[i] = b
        b += delta
        i += 1

    for i in range(n):
        bins = function_kde(x[i], y[i], 3, binpoints)

        for j in range(nbins):
            masterbin[j] += bins[j]

    # Plot the master bin
    plt.plot(binpoints, masterbin)
    plt.plot(x, y)
    plt.show()
