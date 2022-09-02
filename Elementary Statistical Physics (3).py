import numpy as np
import matplotlib.pyplot as plt
import random
N = 10**5
K = 1.38*1e-23  # Boltzmannkonstanten
m = 2*1.6e-27   # Massen til H_2, kilogram
T=3000          # Temperaturen, Kelvin
#middelverdi av abs(V)
def Pvu(a, b, N, T):
    V = np.linspace(a, b, N)
    Dens = np.zeros(len(V))
    for i in range(len(V)):
        Dens[i] = (((m/(2*np.pi*K*T))**(3/2))*4*np.pi*(V[i]**2)*np.exp(-0.5*(m*V[i]**2/(K*T))))*V[i]
    return V,Dens
V,Dens=Pvu(0,3e4,N,T)
dv=V[1]-V[0]
integral=np.trapz(Dens,V,dv)
print(integral) #5739.779892994196 <v> middelverdi

#Trykk fordeling?
def Pp(a, b, N, T):
    V = np.linspace(a, b, N)  # Hastighet for N partikler i x retning
    P = np.zeros(len(V))
    p = np.zeros(len(V))
    n= np.zeros(len(V))
    for i in range(len(V)):
        p[i]=V[i]*m #bevegelses mengde
        P[i] = (1/(2*np.pi*m*K*T))**(3/2)*np.exp(-(p[i]**2/(2*m*K*T)))*4*np.pi*p[i]**2 #trykk fordeling?
        n[i]= (p[i]**2/m)*P[i] #?
    return p,P,n
p,P,n=Pp(0,3e4,N,3000)
dp=p[1]-p[0]
integral=np.trapz(n,p,dp)
K = 1.38*1e-23
trykk=integral*N/3
print(N*K*T)    #4.1399999999999994e-15 (fasit)
print(trykk)    #4.139999999999476e-15 utregning for trykk
E=trykk/N*3/2
print(E)        #utregning fra trykk og bevegelses mengde
print(3/2*K*T)  #fasit
