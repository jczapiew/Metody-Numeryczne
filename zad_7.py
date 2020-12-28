import numpy as np
import matplotlib.pyplot as plt

data = np.loadtxt("measurements18.txt")
px = data[:, 0]
py = data[:, 1]

# okres 1 sekunda
T = 1

F = [[1, 0, T, 0],
     [0, 1, 0, T],
     [0, 0, 1, 0],
     [0, 0, 0, 1]]

G = [[0, 0],
     [0, 0],
     [1, 0],
     [0, 1]]

H = [[1, 0, 0, 0],
     [0, 1, 0, 0]]

P = 5 * np.identity(4)
Q = 0.25 * np.identity(2)
R = 2.0 * np.identity(2)
s = [px[0], py[0], 0, 0]

zx = [0]
zy = [0]

indexes = np.arange(1, len(px), 1)
for i in indexes:
    s = np.dot(F, s)
    P = np.dot(np.dot(F,P), np.transpose(F)) + np.dot(np.dot(G,Q), np.transpose(G))
    z = np.dot(H, s)
    e = [px[i], py[i]] - z
    S = np.dot(np.dot(H,P), np.transpose(H)) + R
    K = np.dot(np.dot(P, np.transpose(H)), np.linalg.inv(S))
    s = s + np.dot(K, e)
    P = np.dot((np.identity(4) - np.dot(K, H)), P)
    zx.append(z[0])
    zy.append(z[1])

predykcja_x = [zx[-1]]
predykcja_y = [zy[-1]]

for i in range(5):
    s = np.dot(F, s)
    P = np.dot(np.dot(F,P), np.transpose(F)) + np.dot(np.dot(G,Q), np.transpose(G))
    z = np.dot(H, s)
    predykcja_x.append(z[0])
    predykcja_y.append(z[1])

plt.plot(px, py, 'bx')
plt.plot(zx, zy, 'r-')
plt.plot(predykcja_x, predykcja_y, 'g--')
plt.plot(predykcja_x[-1], predykcja_y[-1], 'go')
plt.legend(["Pomiary trajektorii", "Wyznaczona trajektoria", "Przewidywana trajektoria"])
plt.show()