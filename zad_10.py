import numpy as np
import matplotlib.pyplot as plt

def funkcja(t, y):
    return (3*t - 4*np.power(t, 2)) * np.sqrt(y)

t0 = 0
n = 100

'''
y = +- (-4/3t^3 + 3/4t^2 + 1)^2
'''

if __name__ == "__main__":
    print("Podaj parametr tk (0, 1.52>:")
    tk = float(input())
    h = tk/n
    t = np.arange(t0, tk, h)
    y1 = np.power(((-1)*(4/3)*np.power(t, 3) + (3/4)*np.power(t, 2) + 1), 2)
    y2 = (-1) * np.power(((-1)*(4/3)*np.power(t, 3) + (3/4)*np.power(t, 2) + 1), 2)

    plt.plot(t, y1)
    plt.plot(t, y2)
    print("Wartosc pochodnej obliczona metoda analityczna:", y1[-1])

    y3 = [1]
    for i in range(len(t) - 1):
        y3.append(y3[i] + funkcja(t[i], y3[i])*h)

    plt.plot(t, y3)
    print("Wartosc pochodnej obliczona metoda Eulera:", y3[-1])

    y4 = [1]
    for i in range(len(t) - 1):
        y0p = funkcja(t[i], y4[i])
        y10 = y4[0] + y0p*h
        y1p = funkcja(t[i+1], y10)
        y4.append(y4[i] + ((y0p + y1p)/2)*h)

    plt.plot(t, y4)
    print("Wartosc pochodnej obliczona metoda Heuna:", y4[-1])

    y5 = [1]
    for i in range(len(t) - 1):
        yi2 = y5[i] + funkcja(t[i], y5[i])*(h/2)
        y5.append(y5[i] + funkcja((t[i]-(h/2)), yi2)*h)
    plt.plot(t, y5)
    print("Wartosc pochodnej obliczona metoda punktu srodkowego:", y5[-1])

    plt.legend(["Metoda analityczna z plusem", "Metoda analityczna z minusem", "Metoda Eulera", "Metoda Heuna",
                "Metoda punktu środkowego"])
    plt.show()