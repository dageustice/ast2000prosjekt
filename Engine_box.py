# IKKE KODEMAL
import ast2000tools.constants
import numpy as np
import matplotlib.pyplot as plt
import random as rng
from numba import jit
from ast2000tools import constants
# inx = np.argwhere(np.abs(pos[:,0])>=num)
# iny = np.argwhere(np.abs(pos[:, 1])>=num)
# konstanter
m = ast2000tools.constants.m_H2

def simulate(N, T, box, NozzleToBoxRatio, Time, dt):
    nozzle_radius = box_side*NozzleToBoxRatio
    momentum = 0
    particles = 0
    N_pos = np.zeros([Time, N, 3])
    N_pos0 = np.zeros([N, 3])
    for i in range(N):
        N_pos0[i][0] = rng.random()*box_side
        N_pos0[i][1] = rng.random()*box_side
        N_pos0[i][2] = rng.random()*box_side
    N_pos[0] = N_pos0
    sigma = np.sqrt(4131*T)
    v0 = np.random.normal(0, sigma, (N, 3))
    for i in range(1, Time):
        for j in range(N):
            N_pos[i][j] = N_pos[i-1][j] + v0[j]*dt
            pos = N_pos[i][j]
            if pos[1] < 0:
                pos_radius = np.sqrt(pos[0]**2+pos[2]**2)
                if pos_radius < nozzle_radius:
                    momentum += v0[j][1]
                    particles += 1
            for k in range(3):
                pos = N_pos[i][j][k]
                if box_side <= pos or pos <= 0:
                    v0[j][k] = -v0[j][k]
    return [N_pos, v0, momentum, particles]


N = int(1e4)
T = 3000
box_side = 1e-6
NozzleToBoxRatio = 1/2*np.sqrt(np.pi)
Time = 1000
dt = 1e-12

N_pos, v0, momentum, particles = simulate(
    N, T, box_side, NozzleToBoxRatio, Time, dt)


print(f"change momentum per second: {-momentum*1e9*10*m}")
print(f"mass loss per second: {particles*10*1e9*m}")

"""
utskrift:

change momentum per second: f1.2620179237607276e-09
mass loss per second: 2.905249680679998e-13

"""

"""
# with open("1e5atoms.xyz", "a") as file:
    for k in range(Time):
        file.write(f"{N+8}\n")
        for j in range(N):
            file.write("\nAr ")
            for i in range(3):
                file.write(f"{N_pos[k][j][i]*1e6} ")
        file.write("\nNe -0.01 -0.01 -0.01")
        file.write("\nNe -0.01 -0.01 1.01")
        file.write("\nNe -0.01 1.01 -0.01")
        file.write("\nNe -0.01 1.01 1.01")
        file.write("\nNe 1.01 -0.01 -0.01")
        file.write("\nNe 1.01 -0.01 1.01")
        file.write("\nNe 1.01 1.01 -0.01")
        file.write("\nNe 1.01 1.01 1.01")
        file.write("\n")
    file.close()
"""
