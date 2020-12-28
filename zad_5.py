import numpy as np
import matplotlib.pyplot as plt
import scipy.linalg as lg

a0 = -0.9
a1 = 3.25
a2 = -3.4

fig, (ax1, ax2) = plt.subplots(2, figsize=(7,7))

A = [[-a2, -a1, -a0],
     [  1,   0,   0],
     [  0,   1,   0]]
B = [1, 0, 0]
C = [1, 1, 1]

# Obliczamy kolejne wartosci sygnalu na wyjsciu ukladu i rysujemy jego wykres
n = np.arange(30)
x = [[0,0,0]]
y = []
for i in range(len(n)):
    x.append(np.dot(A, x[i]) + B)
    y.append(np.dot(C, x[i]))
ax1.plot(n, y)
ax1.set_title("Odpowiedz skokowa ukladu")

# Jak widac na wykresie uklad niestety jest niestabilny

# Implementujemy sterownik optymalny LQR
c1 = 10
c2 = 5
Q = c1 * np.identity(3)
R = c2
P = np.zeros((3,3))
B = np.transpose(np.atleast_2d(B))
for i in range(10):
    P = Q + np.dot(np.dot(np.transpose(A),(P - np.dot(np.dot(np.dot(np.dot(P, B), lg.inv(R + np.dot(np.dot(np.transpose(np.atleast_2d(B)), P), B))), np.transpose(np.atleast_2d(B))), P))), A)
F = np.dot(lg.inv(R + np.dot(np.transpose(np.atleast_2d(B)), np.dot(P,B))), np.dot(np.transpose(np.atleast_2d(B)), np.dot(P, A)))
A_nowe = A - np.dot(B, F)

# Obliczamy sygnal na wyjsciu ukladu dla nowej macierzy stanu oraz rysujemy wykres
B = [1, 0, 0]
C = [1, 1, 1]
u = np.ones(30)
x = [[0,0,0]]
y = []
for i in range(len(n)):
    x.append(np.dot(A_nowe, x[i]) + B)
    y.append(np.dot(C, x[i]))
ax2.plot(n, y)
ax2.plot(n, u)
ax2.legend(["Odpowiedz ukladu", "Pobudzenie ukladu"])
ax2.set_title("Odpowiedz skokowa ukladu ze sterownikiem LQR dla c1 = {} i c2 = {}".format(c1,c2))

"""
        Po przeprowadzeniu kilku konfiguracji stwierdzam, ze c1 przyspiesza uklad i
        zmniejsza jego wzmocnienie, co skutkuje mniejsza amplituda na wyjsciu ukladu.
        Natomiast c2 zwieksza wzmocnienie ale opoznia dzialanie ukladu.
"""

plt.show()