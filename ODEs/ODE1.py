import numpy as np
import matplotlib.pyplot as plt
import scipy as sp
from scipy.integrate import odeint

#Risolviamo ODE nella forma v' = f(t, v)

def dvdt(t, v):
    return -(v - 2)/v

v0 = 1

t = np.linspace(0, 100, 100)
sol = odeint(dvdt, y0=v0, t=t, tfirst=True)

v_sol = sol.T[0]

plt.plot(t, v_sol)
plt.show()