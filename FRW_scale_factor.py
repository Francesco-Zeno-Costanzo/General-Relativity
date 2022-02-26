import numpy as np
import matplotlib.pyplot as plt

#Riscalamento di H per avere l'età in miliardi di anni
H0 =  70
Mpc = 3.085677581e19
km =  1.0
Gyr = 3.1536e16

H_0 = (H0*km*Gyr)/Mpc

def MNL(Omega_0, t):
    '''
    funzione che considera un universo a due componenti:
    materia e costante cosmologica; Omega_0 = Omega_M
    '''
    #tempo del big crunch a cui a = 0
    t_c = (2*np.pi / (3*H_0)) * (1/(np.sqrt(Omega_0 - 1)))

    #per evitare problemi nei calcoli successivi, dell'array
    #dei tempi passato in input si considerano solo i valori minori di t_c
    mask = t < t_c
    t = t[mask]

    #fattore di scala
    a = (np.sqrt(Omega_0 / (Omega_0 - 1))*np.sin((3./2)*H_0*t*np.sqrt(Omega_0 -1 )))**(2./3)

    #età dell'universo
    age = (2. / (3*H_0*np.sqrt(Omega_0 - 1))) * np.arcsin(np.sqrt((Omega_0 - 1)/(Omega_0)))

    #valore massimo di a
    #a_max = (Omega_0 / (Omega_0 - 1))**(1./3)

    return t, a, age, t_c

def Time(x, m, r, l):
    '''
    funzione da integrare numericamente in caso di
    universo con costante cosmologica >= 0
    integrandola si trova t(a) che invertita da a(t)
    '''

    Omega_k = 1 - (m + r + l)
    Omega_R = r/(x**2)
    Omega_M = m/x
    Omega_C = l*x**2
    rho = Omega_R + Omega_M + Omega_C + Omega_k

    t = (1/H_0)*(1/np.sqrt(rho))

    return t


def RK4(num_steps, a0, af, m, r, l):
    '''integratore
    '''

    Age = 0

    t = np.zeros(num_steps + 1)
    a = np.zeros(num_steps + 1)
    a[0] = a0

    da = abs(af-a0)/num_steps

    for i in range(num_steps):

        tk1 = Time(a[i], m, r, l)
        tk2 = Time(a[i] + da/2, m, r, l)
        tk3 = Time(a[i] + da/2, m, r, l)
        tk4 = Time(a[i] + da, m, r, l)
        t[i + 1] = t[i] + (da/6)*(tk1 + 2*tk2 + 2*tk3 + tk4)
        a[i + 1] = a[i] + da

        if(a[i]==1 or 1-da<= a[i] <= 1+da):
            Age = t[i]

    print(f"L'età dell'universo con m={m}, r={r}, l={l} è: {Age:.3f} Gyr")

    return t, a, Age

#mumero di punti e condizione inizale
n = 10000
a_0 = 1e-12
#limite di inetgrazione
a_f = 2.5

print('Per costante cosmologica positiva:')
t0, a0, age0 = RK4(n, a_0, a_f, 0.3, 0, 0.7)
t1, a1, age1 = RK4(n, a_0, a_f, 1, 0, 0)
t2, a2, age2 = RK4(n, a_0, a_f, 0, 0, 1)
t3, a3, age3 = RK4(n, a_0, a_f, 0, 0, 0)
t4, a4, age4 = RK4(n, a_0, a_f, 0, 1, 0)

print('Per costante cosmologica negativa e in assenza di radiazione:')
tp = np.linspace(0, 30, n)
t5, a5, age5, t_c = MNL(2, tp)

print(f"L'età dell'universo è: {age5:.3f} Gyr")
print(f"e la fine dell'universo sarà a: {t_c:.3f} Gyr")

plt.title('Evoluzione del fattore di scala')
plt.plot(t0 - age0, a0, label='$\Lambda CDM: \Omega_{\Lambda}=0.7, \Omega_{M}=0.3$')
plt.plot(t1 - age1, a1, label='Einstein: $ \Omega_{M}=1$')
plt.plot(t2 - age2, a2, label='De Sitter: $\Omega_{\Lambda}=1$')
plt.plot(t3 - age3, a3, label='Vuoto: $\Omega_{k}=1$')
plt.plot(t4 - age4, a4, label='Radiazione: $\Omega_{R}=1$')
plt.plot(t5 - age5, a5, label='Chiuso: $\Omega_{M}=2, \Omega_{\Lambda}=-1$')

plt.xlabel('tempo [Gyr]')
plt.ylabel('a(t)')
plt.xlim(-20, 30)
plt.legend(loc='best')
plt.grid()
plt.show()

