import ast2000tools.constants as const
from ast2000tools.solar_system import SolarSystem
from ast2000tools.space_mission import SpaceMission
from ast2000tools.shortcuts import SpaceMissionShortcuts
import matplotlib.pyplot as plt
import numpy as np
seed = 86752  # insert student's seed number

code_planet_trajectories = 46655  # insert code here

"""------------------------------------------------------------------"""

mission = SpaceMission(seed)
system = SolarSystem(seed)

shortcut = SpaceMissionShortcuts(mission, [code_planet_trajectories])

################################################################
#                 COMPUTE PLANET TRAJECTORIES                  #
################################################################
#                   |      For Part 2      |
#                   ------------------------

"""
Documentation
compute_planet_trajectories(times):

------------------------------------------------------------------------
compute_planet_trajectories() computes the evolution of positions
of each planet in the system over the given times.

Parameters
----------
times  :  array_like
    Array of times for which to obtain the positions, in YEARS.

Returns
-------
planet_positions  :  ndarray
    Array of shape (2, number_of_planets, len(times)) containing the
    positions of the planets in ASTRONOMICAL UNITS.

Raises
------
RuntimeError
    When none of the provided codes are valid for unlocking this method.
------------------------------------------------------------------------

"""

# times must start at 0.
times = np.linspace(0,20,10000)

# Example
# -------
# creating an array with equidistant times between 0 and 2
# years, with 10^5 points.
# times = np.linspace(0, 2, int(1e5))
# -------

planet_positions = shortcut.compute_planet_trajectories(times)
mission.verify_planet_positions(times[-1], planet_positions)

print(planet_positions)

