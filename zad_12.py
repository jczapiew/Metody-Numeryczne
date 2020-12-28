import numpy as np
import matplotlib.pyplot as plt

Ta = 100
h = 0.05
deltax = 2
deltay = 2

A = np.zeros((81, 81))
B = np.zeros(81)

side1 = np.arange(390, 300, -10)
side2 = np.arange(290, 200, -10)

A = np.zeros((81, 81))
for i in range(len(A)):
    A[i, i] += 2 * np.square(deltax) + 2 * np.square(deltax) + h * np.square(deltax) * np.square(deltay)
    if i % 9 != 0: A[i, i - 1] -= np.square(deltay)
    if i % 9 != 8: A[i, i + 1] -= np.square(deltay)
    if int(i / 9) != 0: A[i, i - 9] -= np.square(deltax)
    if int(i / 9) != 8: A[i, i + 9] -= np.square(deltax)

for i in range(81):
    if int(i / 9) == 0: B[i] += side1[i % 9] * np.square(deltax)
    if int(i / 9) == 8: B[i] += side2[i % 9] * np.square(deltax)
    B[i] += Ta * h * np.square(deltax) * np.square(deltay)
    if i % 9 == 0: B[i] += side1[i % 9] * np.square(deltay)
    if i % 9 == 8: B[i] += side2[i % 9] * np.square(deltay)

x = np.linalg.solve(A, B).reshape(9, 9)

plt.title("Rozkład temperatury w węzłach płytki")
plt.pcolor(x, cmap='hot')
bar = plt.colorbar()
bar.set_label("Temperatura")

plt.show()