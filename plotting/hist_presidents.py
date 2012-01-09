#!/usr/bin/env python

import matplotlib.pyplot as plt

if __name__=='__main__':

    x = []
    y = []

    for line in file('presidential_days_in_office.txt'):
        line = line.strip()
        [order, name, daysInOffice] = line.split("\t")
        x.append(order)
        y.append(daysInOffice)

    plt.hist(y)
    plt.show()
