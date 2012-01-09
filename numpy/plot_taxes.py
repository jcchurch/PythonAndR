#!/usr/bin/env python

import matplotlib.pyplot as plt

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

filename = "Tax_Year_2007_County_Income_Data.csv"
grossIncome = []
returns2007 = []
exemptions2007 = []
countyName = []

i = 0
for line in file(filename):
    if i > 0:
        line = line.strip() # Remove new lines
        line = line.replace("$", "") # Remove dollar signs
        parts = line.split(",")
        countyCode = int(parts[1])
        thisCountyReturns = float(parts[4])
        thisGrossIncome = float(parts[6])
        thisCountyName = parts[3]

        if countyCode > 0:
            countyName.append(thisCountyName)
            returns2007.append(float(parts[4]))
            exemptions2007.append(float(parts[5]))
    i += 1

(m, b) = linreg(exemptions2007, returns2007)

px = min(exemptions2007)
qx = max(exemptions2007)

py = px * m + b
qy = qx * m + b

fitx = [px, qx]
fity = [py, qy]

print m, b
print fitx
print fity

new_la = m * 7405456 + b
new_cook = m * 5754875 + b

print new_la
print new_cook

plt.plot(returns2007, exemptions2007, 'r.')
plt.plot(fitx, fity, 'b-')
plt.show()
