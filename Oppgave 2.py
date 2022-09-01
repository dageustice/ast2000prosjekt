import numpy as np
import matplotlib.pyplot as plt
import random
def Q(a, b, N, T):
    Vx = np.linspace(a, b, N)  # Hastighet for N partikler i x retning
    m = 2*1.6e-27
    K = 1.38*1e-23
    o = (K*T)
    sigma = 3520.68
    Dens = np.zeros(len(Vx))
    for i in range(len(Vx)):
        # sannsynlighets tettheten for alle Vx verdier av N partikler
        # Dens[i] = ((m/(np.square(2*np.pi*K*T))))*np.exp((-0.5*m*Vx[i]**2)/(K*T))
        Dens[i] = 1/(np.sqrt(2*np.pi)*sigma)*np.exp(-Vx[i]**2/(2*sigma**2))
        # Dens[i] = (1/(np.square(2*np.pi)*(sigma)))*(np.exp(-Vx[i]**2/(2*(sigma)**2)))
    return Vx, Dens


sigma = 3520.68
# Vx, Dens = Q(-2.5e4, 2.5e4)
Vx, Dens = Q(5e3, 30e3, 10**5, 3000)
Integral = np.zeros(len(Vx+1))
dx = Vx[1]-Vx[0]
integrate = np.trapz(Dens, Vx, dx)
for i in range(len(Vx)-1):
    Integral[i] = dx*(1/2)*(Dens[i]+Dens[i+1])
print(sum(Integral))

plt.plot(Vx/1e4, Dens)
plt.xlabel("10^4 m/s")
plt.show()
