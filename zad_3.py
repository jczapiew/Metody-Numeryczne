import numpy as np
import scipy.linalg as lg

# Spisujemy wszystkie dane ze schematu
Qa = 200
Qb = 300
Qc = 150
Qd = 350
ca = 2
cb = 2
Ws = 1500
Wg = 2500
E12 = 25
E23 = 50
E34 = 50
E35 = 25

# Obliczamy macierze A i B
A = [[E12, -E12, 0, 0, 0],
     [-E12, (E12 + E23), -E23, 0, 0],
     [0, -E23, (E23 + E34 + E35), -E34, -E35],
     [0, 0, -E34, (E34 + Qc), 0],
     [0, 0, -E35, 0, (E35 + Qd)]]
B = [(Ws + Qa*ca), (Qb*cb), 0, 0, Wg]

# Wyznaczamy Lower triangular i Upper triangular z macierzy A
_, L, U = lg.lu(A)
# Wyznaczamy wektor d z rownania Ld = B
d = lg.solve_triangular(L, B, lower=True)
# Wyznaczamy wektor x z rownania Ux = d
x = lg.solve_triangular(U, d)

print("Wektor CO w stanie ustalonym dla poszczegolnych pokoi to:\n", x)

# Ograniczamy ilosc CO pochodzacego z dymu i grilla
Ws1 = 800
Wg1 = 1200

B1 = [(Ws1 + Qa*ca), (Qb*cb), 0, 0, Wg1]
d1 = lg.solve_triangular(L, B1, lower=True)
x1 = lg.solve_triangular(U, d1)

print("Wektor C0 w stanie ustalonym po ograniczeniu C0 z dymu i grilla:\n", x1)

# Wyznaczamy macierz odwrotna A metoda LU
b = [0, 0, 0, 0, 0]
A_do_minus_jeden = []
for i in range(5):
    b[i] = 1
    d = lg.solve_triangular(L, b, lower=True)
    A_do_minus_jeden.append(lg.solve_triangular(U, d))
    b = [0, 0, 0, 0, 0]

A_do_minus_jeden = np.transpose(A_do_minus_jeden)
print("A^(-1) wyznaczone metoda LU:\n", A_do_minus_jeden)

# Udzialy procentowe CO pochodzacego z grilla, papierosow i z ulicy w pokoju dla dzieci
print("Udział CO pochodzacego z grilla: ", ((A_do_minus_jeden[3,4] * Wg)/x[3])*100, "%")
print("Udział CO pochodzacego z papierosow: ", ((A_do_minus_jeden[3,0] * Ws)/x[3])*100, "%")
print("Udział CO pochodzacego z ulicy: ", (((A_do_minus_jeden[3,0] * Qa * ca) + (A_do_minus_jeden[3,1] * Qb * cb))/x[3])*100, "%")