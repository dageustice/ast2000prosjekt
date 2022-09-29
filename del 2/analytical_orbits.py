from solar_system import *
import numpy as np
import matplotlib.pyplot as plt

def rotate2d(vector, theta):
    x = vector[0]
    y = vector[1]
    vector[0] = np.cos(theta)*x-np.sin(theta)*y
    vector[1] = np.sin(theta)*x+np.cos(theta)*y
    return np.array(vector)

def analytical_orbits(semimajoraxis, eccentricity, aphangle,  x0, y0, vx, vy):
    a = semimajoraxis
    e = eccentricity
    print(a)
    print(e)
    b = np.sqrt(a**2 * (1-e**2))
    t = np.linspace(0, 2*np.pi, 100)
    if y0 != 0:
        w = np.arctan(x0*b/y0/a)
    else:
        w = np.arctan(x0*69000690006900069)      # :)
    x = a*np.cos(w+t)
    y = b*np.sin(w+t)
    for i in range(len(t)):
        x[i], y[i] = rotate2d([x[i], y[i]], aphangle)
    plt.plot(x, y)
    plt.plot(posx, posy, "x")


pos = system.initial_positions
vel = system.initial_velocities

print(system.initial_positions)
for i in range(system.number_of_planets):
    sma, e, aa, posx, posy, vx, vy =\
        system.semi_major_axes[i], system.eccentricities[i], \
        system.initial_orbital_angles[i], pos[0][i], pos[1][i], \
        vel[0][i], vel[1][i]
    analytical_orbits(sma, e, aa, posx, posy, vx, vy)

print(system.initial_orbital_angles)
plt.axis("equal")
plt.show()

