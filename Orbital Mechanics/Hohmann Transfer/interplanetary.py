import math as m
import functions as f

mu_sun = f.get_mu('sun')

starting_planet, starting_orbital_radius, target_planet, target_orbital_radius = f.get_input()

print()
r1 = f.orbital_radius[starting_planet]
r2 = f.orbital_radius[target_planet]

a = (r1 + r2) / 2
c = (2 * a) - (2 * r1)
eccentricity = c / a

origin_sphere_of_influence = f.get_orbital_radius(starting_planet) * (f.body_mass[starting_planet] / f.body_mass['sun'])
target_sphere_of_influence = f.get_orbital_radius(target_planet) * (f.body_mass[target_planet] / f.body_mass['sun'])

#Heliocentric
transfer_energy = - mu_sun / (r1 + r2) #epsilon_t
v1 = m.sqrt(2 * ((mu_sun / r1) + transfer_energy)) #heliocentric velocity
v_starting_planet = m.sqrt(mu_sun / r1) #planet one velocity / v0
v_escape_starting = abs(v1 - v_starting_planet)  #v infinity earth

v2 = m.sqrt(2 * ((mu_sun / r2) + transfer_energy)) #
target_velocity = m.sqrt(mu_sun / r2) #v_target

#Departure
v_inf  = v1 - v_starting_planet
escape_energy = (v_inf ** 2) / 2
v0 = m.sqrt(2 * (f.get_mu(starting_planet) / starting_orbital_radius) + escape_energy)

v_starting_park = m.sqrt(f.get_mu(starting_planet) / starting_orbital_radius) #vcs_earth
delta_v_boost = abs(v0 - v_starting_park)

#Arrival
v_inf_target = abs(target_velocity - v2)

energy_target = ((v_inf_target ** 2) / 2)

v_hyperbolic = m.sqrt(2 * ((f.get_mu(target_planet) / target_orbital_radius) + energy_target))

v_target_park = m.sqrt(f.get_mu(target_planet) / target_orbital_radius)
delta_v_retro = abs(v_target_park - v_hyperbolic)

#Total Change
delta_v_mission = delta_v_boost + delta_v_retro

def interplanetary():
    print("Velocity of initial parking orbit:", v_starting_park, "km/s")
    print("Velocity change to enter transfer:", delta_v_boost, "km/s")
    print("Transfer Velocity:", v1, "km/s")
    print("Velocity change to enter target orbit:", delta_v_retro, "km/s")
    print("Total velocity change:", delta_v_mission, "km/s")
    f.TOF(a)