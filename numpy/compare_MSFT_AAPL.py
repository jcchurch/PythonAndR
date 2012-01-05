#!/usr/bin/env python

import numpy as np
import matplotlib.pyplot as plt

# Read the data of AAPL and MSFT
AAPL = np.loadtxt("aapl.csv", delimiter=',', skiprows=1, usecols=[6])
MSFT = np.loadtxt("msft.csv", delimiter=',', skiprows=1, usecols=[6])

# In both datasets, the data is in order from NEWEST to OLDEST.
# To make things plot from OLDEST to NEWEST, we reverse the older.
AAPL = AAPL[::-1]
MSFT = MSFT[::-1]

# Pass the data through a linear transformation.
AAPL_linear = (AAPL - min(AAPL)) / (max(AAPL) - min(AAPL))
MSFT_linear = (MSFT - min(MSFT)) / (max(MSFT) - min(MSFT))

plt.plot(AAPL, 'b-')
plt.plot(MSFT, 'g-')
plt.show()

raw_input()

# Now center the starting points at Zero
AAPL_linear -= AAPL_linear[0]
MSFT_linear -= MSFT_linear[0]

plt.plot(AAPL_linear, 'b-')
plt.plot(MSFT_linear, 'g-')
plt.show()

raw_input()

# Compute the CDF
# This must be done manually
AAPL_CDF = np.cumsum(AAPL)
MSFT_CDF = np.cumsum(MSFT)

AAPL_CDF = (AAPL_CDF - min(AAPL_CDF)) / (max(AAPL_CDF) - min(AAPL_CDF))
MSFT_CDF = (MSFT_CDF - min(MSFT_CDF)) / (max(MSFT_CDF) - min(MSFT_CDF))

plt.plot(AAPL_CDF, 'b-')
plt.plot(MSFT_CDF, 'g-')
plt.show()
