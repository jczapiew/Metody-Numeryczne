import numpy as np
import matplotlib.pyplot as plt

def funkcja1(t, x, y, z):
    return (-10*x + 10*y)

def funkcja2(t, x, y, z):
    return (28*x - y - x*z)

def funkcja3(t, x, y, z):
    return ((-8/3)*z + x*y)

fig1, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2)

t0 = 0
tk = 25
h = 0.03125

x = [5]
y = [5]
z = [5]

t = np.arange(t0, tk, h)

for i in range(len(t) - 1):
    k1x = funkcja1(t[i], x[i], y[i], z[i])
    k1y = funkcja2(t[i], x[i], y[i], z[i])
    k1z = funkcja3(t[i], x[i], y[i], z[i])
    k2x = funkcja1(t[i] + h / 2, x[i] + (k1x * h) / 2, y[i] + (k1y * h) / 2, z[i] + (k1z * h) / 2)
    k2y = funkcja2(t[i] + h / 2, x[i] + (k1x * h) / 2, y[i] + (k1y * h) / 2, z[i] + (k1z * h) / 2)
    k2z = funkcja3(t[i] + h / 2, x[i] + (k1x * h) / 2, y[i] + (k1y * h) / 2, z[i] + (k1z * h) / 2)
    k3x = funkcja1(t[i] + h / 2, x[i] + (k2x * h) / 2, y[i] + (k2y * h) / 2, z[i] + (k2z * h) / 2)
    k3y = funkcja2(t[i] + h / 2, x[i] + (k2x * h) / 2, y[i] + (k2y * h) / 2, z[i] + (k2z * h) / 2)
    k3z = funkcja3(t[i] + h / 2, x[i] + (k2x * h) / 2, y[i] + (k2y * h) / 2, z[i] + (k2z * h) / 2)
    k4x = funkcja1(t[i] + h, x[i] + k3x * h, y[i] + k3y * h, z[i] + k3z * h)
    k4y = funkcja2(t[i] + h, x[i] + k3x * h, y[i] + k3y * h, z[i] + k3z * h)
    k4z = funkcja3(t[i] + h, x[i] + k3x * h, y[i] + k3y * h, z[i] + k3z * h)
    x.append(x[i] + (1/6)*(k1x + 2*k2x + 2*k3x + k4x)*h)
    y.append(y[i] + (1/6)*(k1y + 2*k2y + 2*k3y + k4y)*h)
    z.append(z[i] + (1/6)*(k1z + 2*k2z + 2*k3z + k4z)*h)

ax1.set_title("Przebieg x")
ax1.plot(t, x, color='blue')
ax2.set_title("Przebieg y")
ax2.plot(t, y, color='orange')
ax3.set_title("Przebieg z")
ax3.plot(t, z, color='red')

plt.figure(2)
ax = plt.axes(projection='3d')
ax.set_title("Trajektoria fazowa")
ax.plot3D(x, y, z, color='green')

plt.show()