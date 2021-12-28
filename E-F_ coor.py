import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint


rs = 3      #Schwarzschild radius
r0 = 2.5    #Initial radius

ti = -10    #Initial time
tf = 10     #Final time

num_steps = 10000 #number of integration steps

def eq(r):
    '''equation for incoming rays
    Parameters
    ----------
    r : actual position
    Reurns
    ----------
    speed in present position
    '''
    return (-rs - r)/(r + rs)

def eq1(r):
    '''equation for outgoing rays
    Parameters
    ----------
    r : actual position
    Reurns
    ----------
    speed in present position
    '''
    return (-rs + r)/(r + rs)


def RK4(num_steps, x0, t0, tf, f):
    '''
    Compute solution using runge_kutta4 method.

    Parameters
    ----------
    num_steps : Integer
        number of integration steps.
    x0 : float
        initial radius.
    t0 : float
        initial time of integration.
    tf : float
        final time of integration.
    func : callable
        function to integrate.
    Returns
    -------
    x : one dimensional array
        solution of the equation
    t : one dimensional array
        time
    '''
    x = np.zeros(num_steps + 1)
    t = np.zeros(num_steps + 1)

    x[0], t[0] = x0, t0

    dt = abs(tf-ti)/num_steps

    for i in range(num_steps):
        if x[i] > 0:
            xk1 = f(x[i])
            xk2 = f(x[i] + ek1*dt/2)
            xk3 = f(x[i] + ek2*dt/2)
            xk4 = f(x[i] + ek3*dt)
            x[i + 1] = x[i] + (dt/6)*(xk1 + 2*xk2 + 2*xk3 + xk4)
        else:
            x[i] = 0

        t[i + 1] = t[i] + dt

    return x, t

r_en, t = RK4(num_steps, r0, ti, tf, eq)
r_us, t = RK4(num_steps, r0, ti, tf, eq1)

plt.xlabel('r')
plt.ylabel(r'$\overline{x^0}$')
plt.plot(r_en, t, 'k', label='raggi entranti')
plt.plot(r_us, t, 'r', label='raggi uscenti')
plt.plot(rs*np.ones(len(t)), t, linestyle='--', label='orizzonte')
plt.legend()
plt.grid()
plt.show()