import numpy as np
import matplotlib.pyplot as plt
def Q(a,b):
    N=10**5
    Vx=np.linspace(a,b,N)
    m=1.6e-27*2
    T=3000
    K=1.38*10**-23
    u=np.square(K*T/m)
    Dens=np.zeros(len(Vx))
    for i in range(len(Vx)):
        Dens[i]=((m/(2*np.pi*K*T))**1/2)*np.exp((-m*abs(Vx[i])**2)/(2*K*T))
#        Dens[i]=((1/np.square(2*np.pi)))*np.exp((-m*abs(Vx[i])**2)/(2*K*T))
    return Vx,Dens
Vx,Dens=Q(-2.5e4,2.5e4)
Integral=np.zeros(len(Vx+1))
dx=5/1e5
for i in range(len(Vx)-1):
    Integral[i]=dx*(1/2)*(Dens[i]+Dens[i+1])
print(sum(Integral))

plt.plot(Vx/10**4,Dens)
plt.xlabel("10^4 m/s")
plt.show()