import sys
import math
import matplotlib.pyplot as plt

SQRT_2PI = math.sqrt(2.0 * math.pi)

def gaussian(x):
    return math.exp(-0.5*x*x)/SQRT_2PI

def function_kde(x, y, binpoints):
    bins = [0] * len(binpoints)
    for i in range(len(binpoints)):
        bins[i] = gaussian( (binpoints[i] - x) / float(y) ) / float(y)

    return bins

if __name__=='__main__':

    low = -5.0
    high = 5.0
    nbins = 201

    binpoints = [0] * nbins
    masterbin = [0] * nbins

    delta = (high - low) / (nbins - 1)

    b = low
    i = 0
    while b <= high:
        binpoints[i] = b
        b += delta
        i += 1

    g = function_kde(0, 1, binpoints)

    # Plot the master bin
    plt.plot(binpoints, g)
    plt.show()
