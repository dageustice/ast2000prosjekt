# IKKE KODEMAL
from solar_system import *
import numpy as np
import matplotlib.pyplot as plt
plt.style.use('dark_background')

def rotate2d(vector, theta):    # Denne funksjonen roteter en vektor
    x = vector[0]               # med en gitt vinkel
    y = vector[1]
    vector[0] = np.cos(theta)*x-np.sin(theta)*y
    vector[1] = np.sin(theta)*x+np.cos(theta)*y
    return np.array(vector)

def analytical_orbits(semimajoraxis, eccentricity, aphangle,  x0, y0, theta_0):
    a = semimajoraxis                   # store halvakse
    e = eccentricity                    # eksentrisistet
    b = np.sqrt(a**2 * (1-e**2))        # et uttrykk for b gitt a og e
    t = np.linspace(0, 2*np.pi, 2000)
    # NB
    # Disse tidsstegene svarer IKKE til virkelige tidssteg
    x = a*np.cos(t + theta_0 - aphangle)    # parameterisering av en ellipse
    y = b*np.sin(t + theta_0 - aphangle)
    for i in range(len(t)):
        x[i], y[i] = rotate2d([x[i], y[i]], aphangle)  # roteter ellipsene
    x = x + x0 - x[0]       # flytter ellipsene slik at de matcher
    y = y + y0 - y[0]       # med faktisk posisjon
    if __name__ == "__main__":
        plt.plot(x, y)
        plt.plot(x0, y0, "x")       # test for å se om startposisjon stemmer
        plt.plot(x[0], y[0], "o",   # sirklene skal da overlappe kryssene
                 label=f"planet {int(np.argwhere(system.eccentricities == e))}")


pos = system.initial_positions
vel = system.initial_velocities
if __name__ == "__main__":
    for i in range(system.number_of_planets):   # henter info fra hver planet
        sma, e, aa, posx, posy, theta_0 = \
            system.semi_major_axes[i], system.eccentricities[i], \
            system.aphelion_angles[i], pos[0][i], pos[1][i], \
            system.initial_orbital_angles[i]
        analytical_orbits(sma, e, aa, posx, posy, theta_0)

    plt.axis("equal"); plt.title("Analytiske planetbaner")
    plt.legend(); plt.xlabel("Avstand [AU]")
    plt.ylabel("Avstand [AU]"); plt.savefig("analytiske_planetbaner.png")
    plt.show();

