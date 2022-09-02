import numpy as np
import matplotlib.pyplot as plt
import random as rng

def init_pos(N, box_side):
    N_pos0 = np.zeros([N, 3])
    for i in range(N):
        pos = N_pos0[i]
        pos[0] = rng.random()*box_side
        pos[1] = rng.random()*box_side
        pos[2] = rng.random()*box_side
    return N_pos0


N = int(1e5)
box_side = 1e-6
N_pos0 = init_pos(N, box_side)*1e6

Time = 1000
N_pos = np.zeros([Time, N, 3])
N_vel = np.zeros_like(N_pos)
N_pos[0] = N_pos0


with open("100atoms.xyz", "a") as file:
    file.write(f"{N}\n")
    for j in range(N):
        file.write("\nAr ")
        for i in range(3):
            file.write(f"{N_pos0[j][i]} ")
    file.close()
