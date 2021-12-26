import numpy as np
import matplotlib.pyplot as plt
import scipy as sp
from scipy.integrate import odeint

#ODE del prim'ordine accoppiate sempre nella forma derivata prima = funzione

l = 100 #s.t. r**2 * y2 = l
rs = 3  #Schwarzschild radius

def dSdx(x, S):
    y1, y2 = S
    return [-(y1 - rs)/y1, l/y1**2]

y1_0 = 10
y2_0 = 0
S_0 = (y1_0, y2_0)

x = np.linspace(0, 200, 10000)
sol = odeint(dSdx, y0=S_0, t=x, tfirst=True)

y1_sol = sol.T[0]
y2_sol = sol.T[1]

plt.figure(2)
plt.polar(y2_sol, y1_sol)
plt.savefig('schwarzBH', dpi=1000)
plt.show()
