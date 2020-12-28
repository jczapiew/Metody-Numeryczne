import numpy as np
import matplotlib.pyplot as plt

data = np.loadtxt('data18.txt')
x = data[:, 0]
y = data[:, 1]

plt.plot(x, y, 'o', color='red')

def interpolacjaNewtona(x, y):
    iterations = np.arange(len(x) - 1, 0, -1)
    y1 = np.copy(y)
    bees = [y1[0]]
    for i in iterations:
        y2 = np.copy(y1)
        y1 = np.zeros(i)
        for j in range(i):
            i1 = len(x) - i
            y1[j] = (y2[j + 1] - y2[j])/(x[j+i1] - x[j])
        bees.append(y1[0])
    x1 = np.arange(np.amin(x), np.amax(x), 0.001)
    y1 = np.zeros(len(x1))
    for i in range(len(bees)):
        yi = np.ones(len(y1))
        for j in range(i):
            yi *= x1 - x[j]
        y1 += bees[i]*yi
    return x1, y1

def funkcjeSklejane(x, y):
    a1 = np.zeros((len(y), len(x)))
    b1 = np.zeros(len(x))
    a1[0, 0] = 1
    a1[-1, -1] = 1
    for i in range(1, len(x) - 1, 1):
        a1[i, i-1] = x[i] - x[i - 1]
        a1[i, i] = 2 * (x[i] - x[i - 1] + x[i + 1] - x[i])
        a1[i, i+1] = x[i + 1] - x[i]
        b1[i] = 3 * ((y[i + 1] - y[i])/(x[i + 1] - x[i]) - (y[i] - y[i - 1])/(x[i] - x[i - 1]))
    c = np.linalg.solve(a1, b1)
    ind = np.arange(len(x)-1, dtype=np.uint8)
    a = np.zeros(len(ind))
    b = np.zeros(len(ind))
    d = np.zeros(len(ind))
    h = np.zeros(len(ind))
    a[ind] = y[ind]
    h[ind] = x[ind + 1] - x[ind]
    b[ind] = (y[ind + 1] - y[ind])/h[ind] - (h[ind]/3) * (2*c[ind] + c[ind + 1])
    d[ind] = (c[ind + 1] - c[ind])/(3*h[ind])
    x2 = np.arange(np.amin(x), np.amax(x), 0.001)
    iis = np.zeros_like(x2, dtype=np.uint8)
    for i in range(len(x)):
        iis[x2 >= x[i]] = i
    y2 = a[iis] + b[iis]*(x2 - x[iis]) + c[iis]*np.power((x2 - x[iis]), 2) + d[iis]*np.power(x2 - x[iis], 3)
    return x2, y2

x1, y1 = interpolacjaNewtona(x, y)
plt.plot(x1, y1, '-', color='orange')

x2, y2 = funkcjeSklejane(x, y)
plt.plot(x2, y2, '-', color='green')

plt.legend(["Dane pomiarowe", "Wielomian interpolacyjny Newtona", "Funkcje sklejane trzeciego rzedu"])
plt.show()