import ast2000tools.constants as const
import ast2000tools.utils as utils
from ast2000tools.space_mission import SpaceMission
from solar_system import *
import matplotlib.pyplot as plt
import numpy as np

G=const.G_sol
X=system.initial_positions
V=system.initial_velocities
StjerneM=system.star_mass


def a(dis):
    return G*StjerneM/dis


def simulate_orbits(duration, n_time_steps_per_year):
    Tid=np.linspace(0,duration,n_time_steps_per_year) #brukes ikke
    
    R=np.zeros((2,7,n_time_steps_per_year))
    
    H=np.zeros((2,7,n_time_steps_per_year))
    ax=np.zeros((7,n_time_steps_per_year))
    ay=np.zeros((7,n_time_steps_per_year))
    dt=Tid[1]-Tid[0]

#Setter inn initial verdiene i x,y retningene for hastighet og posisjon i
#en større matrise med formen 2x7x10000
    
    for i in range(system.number_of_planets):
        
        R[0][i][0],R[1][i][0]=X[0][i],X[1][i] #for t=0 angir posisjon i x,y retning
        
        H[0][i][0],H[1][i][0]=V[0][i],V[1][i] #for t=0 angir hastighet i x,y retning

    for j in range(n_time_steps_per_year-1):
        for i in range(system.number_of_planets):    
            theta=np.arctan(R[1][i][j]/R[0][i][j])
            distance=np.sqrt(((R[0][i][j]**2)+(R[1][i][j]**2)))
            Force=a(distance)
            ax[i][0]=np.cos(theta)*Force      
            ay[i][0]=np.sin(theta)*Force
           # ax[i][j+1]=-H[0][i][j]-R[0][i][j]
            #ay[i][j+1]=-H[1][i][j]-R[1][i][j]
            H[0][i][j+1]=H[0][i][j]+(ax[i][j]+ax[i][j+1])*0.5*dt
            H[1][i][j+1]=H[1][i][j]+(ay[i][j]+ay[i][j+1])*0.5*dt
            R[0][i][j+1]=R[0][i][j]+H[0][i][j]*dt+0.5*ax[i][j]*dt**2
            R[1][i][j+1]=R[1][i][j]+H[1][i][j]*dt+0.5*ay[i][j]*dt**2
        
                
    return Tid, R,theta,H
Time,ppos,theta,VV=simulate_orbits(20,10000)

print(ppos)
plt.plot(ppos[0],ppos[1])