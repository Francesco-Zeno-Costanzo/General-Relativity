import numpy as np
import matplotlib.pyplot as plt
import scipy as sp
from scipy.integrate import odeint

#ODE del prim'ordine accoppiate sempre nella forma derivata prima = funzione

def dSdx(x, S):
    y1, y2 = S
    return [(y1 - 3)/y1, 1000/y1**2]

y1_0 = 10
y2_0 = 0
S_0 = (y1_0, y2_0)

x = np.linspace(0, 200, 10000)
sol = odeint(dSdx, y0=S_0, t=x, tfirst=True)

y1_sol = sol.T[0]
y2_sol = sol.T[1]

'''
plt.figure(1)
plt.plot(x, y1_sol)
plt.plot(x, y2_sol%(2*np.pi))
'''
plt.figure(2)
plt.polar(y2_sol, y1_sol)
#plt.savefig('schwarzWH', dpi=1000)
plt.show()
