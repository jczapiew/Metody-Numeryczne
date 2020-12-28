import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import fmin

data = np.loadtxt("data11.txt")
x = data[:,0]
y = data[:,1]
plt.plot(x,y)

def odpowiedz_skokowa(tau, zeta, x):
    y1 = 1 - ((np.exp((-zeta/tau)*x)/np.sqrt(1-zeta*zeta))*np.sin((np.sqrt(1-zeta*zeta)/tau)*x + np.arctan(np.sqrt(1-zeta*zeta)/zeta)))
    return y1

def odpowiedz_impulsowa(tau, zeta, x):
    y2 = (np.exp((-zeta/tau)*x)/(tau*np.sqrt(1-zeta*zeta)))*np.sin((np.sqrt(1-zeta*zeta)/tau)*x)
    return y2

def odpowiedz(k, tau, tau_z, zeta, x):
    skok = odpowiedz_skokowa(tau, zeta, x)
    imp = odpowiedz_impulsowa(tau, zeta, x)
    odpowiedz = k * (tau_z * imp + skok)
    return odpowiedz

def regresja(params):
    k, tau, tau_z, zeta = params
    odp = odpowiedz(k, tau, tau_z, zeta, x)
    regression = np.sum(np.square(y - odp))
    return regression

k = 0.75
tau = 1
tau_z = -0.75
zeta = 0.6

parameters = fmin(regresja, [k, tau, tau_z, zeta])
print("Parametry układu to:")
print("k = {}".format(parameters[0]))
print("tau = {}".format(parameters[1]))
print("tau_z = {}".format(parameters[2]))
print("zeta = {}".format(parameters[3]))

odp1 = odpowiedz(parameters[0], parameters[1], parameters[2], parameters[3], x)

plt.plot(x, odp1)
plt.legend(["Odpowiedz skokowa ukladu z pliku txt", "Odpowiedz skokowa wyznaczonego ukladu"])
plt.show()