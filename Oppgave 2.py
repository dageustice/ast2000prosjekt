import numpy as np
import matplotlib.pyplot as plt
import random
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
        # Dens[i] = (1/(np.square(2*np.pi)*(sigma)))*(np.exp(-Vx[i]**2/(2*(sigma)**2)))
    return Vx, Densx

# Vx, Dens = Q(-2.5e4, 2.5e4)
N=10**5
Vx, Densx = Pvx(-2.5e4, 2.5e4, N, 3000)
Integral = np.zeros(len(Vx+1))
dx = Vx[1]-Vx[0]
integrate = np.trapz(Densx, Vx, dx)
for i in range(len(Vx)-1):
    Integral[i] = dx*(1/2)*(Densx[i]+Densx[i+1])
print(sum(Integral)*N)
print(integrate*N)
"""plt.plot(Vx/1e4, Densx)
plt.xlabel("10^4 m/s")
plt.show()"""
Vx, Densx = Pvx(5e3, 30e3, N, 3000)
dx = Vx[1]-Vx[0]
integrate = np.trapz(Densx, Vx, dx)
print(integrate)#0.08224984975151238 sannsynligheten for at vi finner partikler med gitt hastighet [5,30]*10**3
print(integrate*N) #8224.984975151237 antall partikler mellom hastighetene [5,30]*10**3
def Pv(a, b, N, T):
    V = np.linspace(a, b, N)  # Hastighet for N partikler i x retning
    m = 2*1.6e-27
    K = 1.38*1e-23
    o = (K*T)
    sigma = np.sqrt(o/m)
    dv=V[1]-V[0]
    Dens = np.zeros(len(V))
    Integral = np.zeros(len(V))
    for i in range(len(V)-1):
        # sannsynlighets fordeling for alle abs(V) verdier av N partikler
        Dens[i] = ((m/(2*np.pi*K*T))**3/2)*np.exp(-m*V[i]**2/(2*K*T))*(4*np.pi*V[i]**2)
        Integral[i] = dv*(1/2)*(Dens[i]+Dens[i+1])
       #feil i utregning altfor lav sannsynlighet
    
    return V, Integral
V,Dens=Pv(0,3e4, N, 3000)
print(Dens)
plt.plot(V, Dens)
#plt.xlabel("10^4 m/s")
plt.show() 


#middelverdi (ikke ferdig)

def Pv(a, b, N, T):
    V = np.linspace(a, b, N)  # Hastighet for N partikler i x retning
    m = 2*1.6e-27
    K = 1.38*1e-23
    o = (K*T)
    sigma = np.sqrt(o/m)
    dv=V[1]-V[0]
    Dens = np.zeros(len(V))
    for i in range(len(V)-1):
        # sannsynlighets fordeling for alle abs(V) verdier av N partikler
        Dens[i] = ((m/(2*np.pi*K*T))**3/2)*np.exp(-m*V[i]**2/(2*K*T))*(4*np.pi*V[i]**2)*V[i]
    Integral=np.trapz(Dens, V, dv)
       
    
    return V, Integral
v,u=Pv(0,10*20,N,3000)
print(u)
#sannsynlighet for bevegelses mengden

def Pp(a, b, N, T):
    V = np.linspace(a, b, N)  # Hastighet for N partikler i x retning
    m = 2*1.6e-27
    
    K = 1.38*1e-23
    P = np.zeros(len(V))
    p = np.zeros(len(V))
    n= np.zeros(len(V))
    for i in range(len(V)):
        p[i]=V[i]*m
        P[i] = (1/(2*np.pi*m*K*T))**(3/2)*np.exp(-(p[i]**2/(2*m*K*T)))*4*np.pi*p[i]**2 #sannsynlighet for p
        n[i]= (p[i]**2/m)*P[i]
    return p,P,n
V,Dens,n=Pp(0,3e4,6*10**18,3000)
dp=V[1]-V[0]
integral=np.trapz(n,V,dp)
K = 1.38*1e-23
print(integral*N/3)
print(N*K*3000)
