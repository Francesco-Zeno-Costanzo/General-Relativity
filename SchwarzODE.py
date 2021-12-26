import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

'''
We want to solve a system of two coupled first-order equations:
y1' = f(...)
y2' = f(...)
'''


l = 100
'''
s.t. r**2 * y2 = l
l is proportional to angular momentum
'''
rs = 3  #Schwarzschild radius

def dSdx(x, S):
    '''System of equations to solve
    '''
    r, phi = S
    dSdx = [-(r - rs)/r, (l/r**2)*((r - rs)/r)]
    return dSdx

#initial condition
r_0 = 10
phi_0 = 0
S_0 = (r_0, phi_0)

#time of integration
x = np.linspace(0, 50, 10000)

sol = odeint(dSdx, y0=S_0, t=x, tfirst=True)

'''
it could be written like this:
r = sol[:,0]
phi = sol[:,1]
But using the transpose we can more easily identify the solutions.
'''
r = sol.T[0]
phi = sol.T[1]

t=np.linspace(0, 2*np.pi, 1000)
a = np.ones(len(t))
plt.figure(1)
plt.polar(t, rs*a, 'k', label="event horaizon") #event horaizon
plt.polar(phi, r, label ="trajectory ")
plt.title("trajectory of a photon around a black hole")
#plt.savefig('schwarzBH', dpi=1000)
plt.legend()

plt.figure(2)
plt.title("radius and angle as a function of time")
plt.plot(x, phi, 'k', label="$\phi(t)$")
plt.plot(x, r, 'r', label="r(t)")
plt.grid()
plt.legend()

plt.figure(3)
plt.title("trajectory of a photon around a black hole")
t=np.linspace(0, 2*np.pi, 1000)
plt.plot(rs*np.cos(t), rs*np.sin(t), 'k', label="event_horaizon") #event horaizon
a = r*np.cos(phi)
b = r*np.sin(phi)
plt.plot(a, b, label ="trajectory ")
plt.grid()
plt.legend()

plt.show()
