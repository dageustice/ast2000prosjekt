import ast2000tools as ast
import ast2000tools.space_mission
import ast2000tools.utils as utils
from ast2000tools.solar_system import SolarSystem
from ast2000tools.space_mission import SpaceMission
from ast2000tools import constants as cons
seed = 86752
# dette lille frøet her er hentet fra brukernavnet
# til et av prosjektarbeidspartnerne. Brukernavnet
# skjules for å bevare anonymiteten.

mission = SpaceMission(seed)
system = SolarSystem(seed)

m_e = 5.972e24
r_e = 6371
mission = SpaceMission(seed)
system = SolarSystem(seed)

if __name__ == "__main__":
    print('My system has a {:g} solar mass star with a radius of {:g} kilometers.'
          .format(system.star_mass, system.star_radius))

    print("mass, radius and SM axis measured in Earth's units")
    for i in range(system.number_of_planets):
        print(f'Planet {i}: {system.types[i]}, '
              f'Mass = {system.masses[i]*cons.m_sun/m_e:.3f}, '
              f'Radius = {system.radii[i]/r_e:.2f},'
              f' semi-major axis = {system.semi_major_axes[i]}')

    SolarSystem.print_info(system)
