import numpy as np
import matplotlib.pyplot as plt
import random
N=10**5
K = 1.38*1e-23
#maxwell dist av hastighet i x retning
def Pvx(a, b, N, T):
    Vx = np.linspace(a, b, N)  # Hastighet for N partikler i x retning
    m = 2*1.6e-27
    K = 1.38*1e-23
    o = (K*T)
    sigma = np.sqrt(o/m)
    Densx = np.zeros(len(Vx))
    for i in range(len(Vx)):
        # sannsynlighets tettheten for alle Vx verdier av N partikler
        Densx[i] = 1/(np.sqrt(2*np.pi)*sigma)*np.exp(-Vx[i]**2/(2*sigma**2))
    return Vx, Densx
Vx, Densx = Pvx(-2.5e4, 2.5e4, N, 3000)
Integral = np.zeros(len(Vx+1))
dx = Vx[1]-Vx[0]
integrate = np.trapz(Densx, Vx, dx)
for i in range(len(Vx)-1):
    Integral[i] = dx*(1/2)*(Densx[i]+Densx[i+1])
print(sum(Integral)*N) #99999.9999994327
print(integrate*N) #99999.99999963594
plt.plot(Vx/1e4, Densx)
plt.xlabel("10^4 m/s")
plt.show()

#maxwell dist av fart
def Pv(a, b, N, T):
    V = np.linspace(a, b, N)  # Fart for N partikler i x,y,z posisjon
    m = 2*1.6e-27
    K = 1.38*1e-23
    Dens = np.zeros(len(V))
    dv=V[1]-V[0] #prøvde å gange inn dv tidligere
    for i in range(len(V)):
        # sannsynlighets fordeling for alle abs(V) verdier av N partikler
        Dens[i] = (((m/(2*np.pi*K*T))**(3/2))*4*np.pi*(V[i]**2)*np.exp(-0.5*(m*V[i]**2/(K*T))))
        
    return V, Dens
V,Dens=Pv(0,3e4, N, 3000)
dv=V[1]-V[0]
integrate = np.trapz(Dens, V, dv)
print(integrate) #0.9999999999999943
plt.plot(V, Dens)
plt.show() 
