# IKKE KODEMAL
import ast2000tools.constants
import numpy as np
import matplotlib.pyplot as plt
import random as rng
from numba import jit
from ast2000tools import constants

k = ast2000tools.constants.k_B
m = ast2000tools.constants.m_H2
print(np.sqrt(k*3000/m))
@jit(nopython=True)
def simulate(N, T, box, NozzleToBoxRatio, Time, dt):
    nozzle_radius = box_side * NozzleToBoxRatio / 2
    # lengden på radius som et forhold til lengden til boksen
    momentum = 0
    particles = 0
    N_pos = np.zeros((Time, N, 3), dtype=np.float64)
    N_pos0 = np.zeros((N, 3), dtype=np.float64)
    for i in range(N):  # lager tilfeldig fordelt partikler i boksen
        # når N er stor, vil partiklene ha en uniform fordeling.
        N_pos0[i][0] = rng.random() * box_side
        N_pos0[i][1] = rng.random() * box_side
        N_pos0[i][2] = rng.random() * box_side
    N_pos[0] = N_pos0
    sigma = np.sqrt(4131 * T)  # skriver 4131 for å hindre feil med små/store tall
    v0 = np.random.normal(0, sigma, (N, 3))  # Maxwell boltzmann fordeling av farten
    for i in range(1, Time):
        for j in range(N):
            N_pos[i][j] = N_pos[i - 1][j] + v0[j] * dt
            pos = N_pos[i][j]
            if pos[1] < 0:
                pos_radius = np.sqrt(pos[0] ** 2 + pos[2] ** 2)
                if pos_radius < nozzle_radius:
                    momentum += v0[j][1]
                    particles += 1
            for k in range(3):
                pos = N_pos[i][j][k]
                if box_side <= pos or pos <= 0:
                    v0[j][k] = -v0[j][k]
    return (N_pos, v0, momentum, particles)


N = int(1e5)
T = 3000
box_side = 1e-6
# NozzleToBoxRatio = 1/(2*np.sqrt(np.pi)) # Hvis vi ønsker 0.25L^2
NozzleToBoxRatio = 1
Time = 1000
dt = 1e-12

N_pos, v0, momentum, particles = simulate(
    N, T, box_side, NozzleToBoxRatio, Time, dt)
print("For a single box unit:")
print(f"change momentum per second: {-momentum * 1e9* m} m/s^2")
print(f"mass loss per second: {particles * 1e9 * m} kg/s")



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
