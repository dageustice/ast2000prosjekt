import numpy as np
import matplotlib.pyplot as plt
import random as rng
from math import acos
import time as time

k = 1.38*1e-23
m = 2*1.67*1e-27
T = 3000
a = np.zeros(1000)
for i in range(1000):
    a[i] = np.abs(rng.gauss(5739, 3520))

print(sum(a)/len(a))
a = time.time()
def init_pos(N, box_side):
    N_pos0 = np.zeros([N, 3])
    for i in range(N):
        pos = N_pos0[i]
        pos[0] = rng.random()*box_side
        pos[1] = rng.random()*box_side
        pos[2] = rng.random()*box_side
    return N_pos0

def rng_point_sphere():
    # funkjsonen returnerer et punkt på enhetssirklen
    u = 2*np.pi * rng.random()
    v = acos(2 * rng.random() - 1)
    x = np.cos(u) * np.sin(v)
    y = np.sin(u) * np.sin(v)
    z = np.cos(v)
    # x, y, z = np.random.normal(0, 3520, 3)
    vec = np.array([x, y, z])
    return vec


def init_vel(N):
    """v0 = np.random.normal(0, 3520, (N, 3))
    vx0 = v0[:, 0]
    vy0 = v0[:, 1]
    vz0 = v0[:, 2]"""
    N_vel0 = np.zeros([N, 3])
    for i in range(N):
        direction = rng_point_sphere()
        v = np.abs(rng.gauss(5739, 3520))
        N_vel0[i] = direction * v

    return N_vel0


def nozzle(pos, vel):
    momentum, particles = 0, 0
    if pos[1] < 0:
        if 0.25*box_side < pos[0] < 0.75*box_side:
            if 0.25*box_side < pos[2] < 0.75*box_side:
                momentum = vel[1]
                particles = 1

    return [momentum, particles]


N = int(100)

box_side = 1e-6
v = 5739.78
N_pos0 = init_pos(N, box_side)
Time = 1000
dt = 1e-12
N_pos = np.zeros([Time, N, 3])

N_pos[0] = N_pos0
momentum = 0
particles = 0
N_vel = init_vel(N)
for i in range(1, Time):
    for j in range(N):
        N_pos[i][j] = N_pos[i-1][j] + N_vel[j]*dt
        mp = nozzle(N_pos[i][j], N_vel[j])
        momentum += mp[0]
        particles += mp[1]
        for k in range(3):
            pos = N_pos[i][j][k]
            if box_side <= pos or pos <= 0:
                N_vel[j][k] = -N_vel[j][k]
print(N_vel)
print(momentum)
print(particles)
b = time.time()
print(b-a)
print((b-a)/60)

"""
Når:
N = int(1e5)
box_side = 1e-6
v = 5739.78
N_pos0 = init_pos(N, box_side)
Time = 1000
dt = 1e-12

Fikk:

total momentum = 450634.43

antall partikler ut = 36630
"""

with open("100atoms.xyz", "a") as file:
    for k in range(Time):
        file.write(f"{N}\n")
        for j in range(N):
            file.write("\nAr ")
            for i in range(3):
                file.write(f"{N_pos0[j][i]*1e6} ")
        file.write("\n")
    file.close()
