# IKKE KODEMAL
import numpy as np
import random as rng
from numba import jit
from ast2000tools import constants as cons

@jit(nopython=True)
def simulate(N, T, box, NozzleToBoxRatio, Time, dt):
    sigma = np.sqrt(cons.k_B * T / cons.m_H2)  # StanDev for
    # StanDev for maxwell-boltzmann distribusjonen
    nozzle_radius = box * NozzleToBoxRatio / 2
    # størrelse på radius i forhold til 1/2 bokslengde
    momentum = 0
    particles = 0
    N_pos = np.zeros((Time, N, 3), dtype=np.float64)
    N_pos0 = np.zeros((N, 3), dtype=np.float64)
    # da har vi alle konstanter, nå kan vi loope:
    for i in range(N):  # lager tilfeldig fordelt partikler i boksen
        # når N er stor, vil partiklene ha en uniform fordeling.
        N_pos0[i][0] = rng.random() * box
        N_pos0[i][1] = rng.random() * box
        N_pos0[i][2] = rng.random() * box
    N_pos[0] = N_pos0  # initialposisjon til partiklene
    v0 = np.random.normal(0, sigma, (N, 3))  # Maxwell boltzmann fordeling av farten
    for i in range(1, Time):
        for j in range(N):
            N_pos[i][j] = N_pos[i - 1][j] + v0[j] * dt
            pos = N_pos[i][j]   # forkorter variabelen
            if pos[1] < 0:
                pos_radius = np.sqrt(pos[0] ** 2 + pos[2] ** 2)
                if pos_radius < nozzle_radius:
                    momentum += v0[j][1]    # bevegelsesmengden til partikkelen
                    particles += 1          # teller antal unnslippede partikler
        for k in range(3):  # sjekker om partikkelen er utenfor boksen
            pos = N_pos[i][j][k]
            if box <= pos or pos <= 0:
                v0[j][k] = -v0[j][k]  # kollisjon <=> fortegnsskifte
    return (N_pos, v0, -momentum*cons.m_H2/(Time*dt),
            particles*cons.m_H2/(Time*dt))


def fuel_burnt(ccArea, box, rocketthrustforce, fuelmass, fuel_consumption,
               rocketmass, speedboost):
    B = ccArea/(box**2)     # tversnittarealet / boksareal = antall bokser
    v = 0   # startfart til raketten
    M = rocketmass + fuelmass
    fuelburned = 0
    i = 1
    dt = 1e-3
    while v <= speedboost:
        a = B*rocketthrustforce/M
        v += a*dt
        fuelburned += B*fuel_consumption*dt  # fuel brukt øker for hver dt
        M -= B*fuel_consumption*dt  # massen minker for hver dt
        if fuelburned > fuelmass:

            print("Burned up all the fuel!")
            print(f"Final velocity: {v:.2f}")
            print(f"{i*dt:.0f} seconds after boosting")
            break
        i += 1
    return fuelburned, fuelmass-fuelburned, (dt*i), v
