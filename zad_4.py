import numpy as np
import matplotlib.pyplot as plt

# Rozwiązania równania: P0 = (-3,65; -2,08), P1 = (-1,945; -1,06), P2 = (0,197; -8,02)
x = np.arange(-4, 1, 0.001)
y1 = -x*x - 5*x - 7
# Z drugiego wzoru wynika, że x != 0,2
x1 = np.arange(-4, 0.199, 0.001)
y21 = (-3*x1*x1)/(1 - 5*x1)
x2 = np.arange(0.201, 1, 0.002)
y22 = (-3*x2*x2)/(1 - 5*x2)

labels = ["y = -x^2 - 5x - 7", "y = -3x^2 + 5xy"]
plt.plot(x,y1)
plt.plot(x1,y21, color='red')
plt.plot(x2,y22, color='red')
plt.legend(labels)

# Znajdujemy rozwiazanie P3 za pomoca interacyjnego podstawiania:
iteracje = 10
xx = 0
for i in range(iteracje):
    yy = -xx*xx - 5*xx - 7
    xx = (yy + 3*xx*xx)/(5*yy)

print("Rozwiazanie P3 ukladu rownan metoda iteracyjnego podstawiania po {} iteracjach wynosi ({}, {})".format(iteracje, xx, yy))

# Znajdujemy wszystkie rozwiazania za pomoca metody Newtona-Raphsona
punkty_poczatkowe = [(-4, -3), (-2, -1), (0,-7)]
for i in range(len(punkty_poczatkowe)):
    xx = punkty_poczatkowe[i][0]
    yy = punkty_poczatkowe[i][1]
    for j in range(iteracje):
        df1_po_x = 2*xx + 5
        df1_po_y = 1
        df2_po_x = 6*xx - 5*yy
        df2_po_y = -5*xx + 1
        jakob = (df1_po_x*df2_po_y) - (df1_po_y*df2_po_x)
        f1 = yy + xx*xx + 5*xx + 7
        f2 = yy + 3*xx*xx - 5*xx*yy
        xx = xx - (f1*df2_po_y - f2*df1_po_y)/jakob
        yy = yy - (f2*df1_po_x - f1*df2_po_x)/jakob
    print("Rozwiazanie ukladu rownan metoda N-R dla punktu poczatkowego {}\n"
          " po {} iteracjach wynosi ({}, {})".format(punkty_poczatkowe[i], iteracje, xx, yy))

plt.show()