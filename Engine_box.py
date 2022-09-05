import numpy as np
import matplotlib.pyplot as plt
import random as rng
from math import acos
import time as time

k = 1.38*1e-23
m = 2*1.67*1e-27
T = 3000



a = time.time()
def init_pos(N, box_side):
    N_pos0 = np.zeros([N, 3])
    for i in range(N):
        pos = N_pos0[i]
        pos[0] = rng.random()*box_side
        pos[1] = rng.random()*box_side
        pos[2] = rng.random()*box_side
    return N_pos0



def init_vel(N):
    v0 = np.random.normal(0, 3520, (N, 3))
    """vx0 = v0[:, 0]
    vy0 = v0[:, 1]
    vz0 = v0[:, 2]"""

    return v0


def nozzle(pos, vel):
    momentum, particles = 0, 0
    if pos[1] < 0:
        if 0.25*box_side < pos[0] < 0.75*box_side:
            if 0.25*box_side < pos[2] < 0.75*box_side:
                momentum = vel[1]
                particles = 1

    return [momentum, particles]


N = int(100)
v0=init_vel(N)

box_side = 1e-6
v = 5739.78
N_pos0 = init_pos(N, box_side)
Time = 1000
dt = 1e-12
N_pos = np.zeros([Time, N, 3])

N_pos[0] = N_pos0
momentum = 0
particles = 0
for i in range(1, Time):
    for j in range(N):
        N_pos[i][j] = N_pos[i-1][j] + v0[j]*dt
        mp = nozzle(N_pos[i][j], v0[j])
        momentum += mp[0]
        particles += mp[1]
        for k in range(3):
            pos = N_pos[i][j][k]
            if box_side <= pos or pos <= 0:
                v0[j][k] = -v0[j][k]
print(N_pos[0])                
