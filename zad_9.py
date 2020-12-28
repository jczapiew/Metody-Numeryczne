import numpy as np

def rombergiem(a4, a3, a2, a1, a0, x1, x2, n):
    h = (x2-x1)/n
    x11 = np.arange(x1, x2, h)
    x22 = np.arange(x1+h, x2+h, h)
    wartosci1 = a4*np.power(x11, 4) + a3*np.power(x11, 3) + a2*np.power(x11, 2) + a1*x11 + a0
    wartosci2 = a4*np.power(x22, 4) + a3*np.power(x22, 3) + a2*np.power(x22, 2) + a1*x11 + a0
    return n, h, np.sum(((wartosci1 + wartosci2)*h)/2)

x1 = -9
x2 = 5
a0 = 3.673
a1 = -2.31
a2 = 0.8672
a3 = -0.5421
a4 = -0.08675

analityczna = (a4/5)*np.power(x2,5) + (a3/4)*np.power(x2,4) + (a2/3)*np.power(x2,3) + (a1/2)*np.power(x2,2) + \
              (a0/1)*np.power(x2,1) - ((a4/5)*np.power(x1,5) + (a3/4)*np.power(x1,4) + (a2/3)*np.power(x1,3) +
                                       (a1/2)*np.power(x1,2) + (a0/1)*np.power(x1,1))
print("")
print("Wynik calki obliczonej analitycznie: {}".format(analityczna))
print("Oraz jej wspolczynniki: a5 = {}, a4 = {}, a3 = {}, a2 = {}, a1 = {}\n".format(a4/5, a3/4, a2/3, a1/2, a0))

blad = 1
iteracja = 1
print("Calkowanie metoda Romberga")
print("Liczba segmentow    h                 calka                        blad [%]")
while blad > 0.2:
    segmenty, h, analityczna1 = rombergiem(a4, a3, a2, a1, a0, x1, x2, np.power(2,iteracja))
    _, _, analityczna2 = rombergiem(a4, a3, a2, a1, a0, x1, x2, np.power(2, iteracja+1))
    romberg = (4/3)*analityczna1 - (1/3)*analityczna2
    blad = np.abs((analityczna - romberg)/analityczna) * 100
    print("       {}           {}           {}           {}".format(segmenty, np.round(h,5), romberg, blad))
    iteracja += 1
print("")

c = [5/9, 8/9, 5/9]
t = np.array([-1*np.sqrt(3/5), 0, np.sqrt(3/5)])
xg = ((x2 + x1) + (x2 - x1)*t)/2
dxg = (x2 - x1)/2

gaussa = np.sum(c*(a4*np.power(xg, 4) + a3*np.power(xg, 3) + a2*np.power(xg, 2) + a1*xg + a0)*dxg)

print("Wynik calki obliczonej trzypunktowa kwadratura Gaussa: {}".format(gaussa))