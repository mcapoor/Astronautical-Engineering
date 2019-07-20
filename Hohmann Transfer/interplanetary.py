import math as m
import functions as f

mu_sun = f.get_mu('sun')

starting_planet = input("Which body are we starting from? ")
starting_orbital_radius = float(input("What is the initial altitude of the parking orbit? ")) + f.body_radius[starting_planet]

target_planet = input("Which body are we going to? ")
target_orbital_radius = float(input("What is the altitude of the parking orbit on the target planet? ")) + f.body_radius[target_planet] #rpt
print()
r1 = f.orbital_radius[starting_planet]
r2 = f.orbital_radius[target_planet]

a = (r1 + r2) / 2
c = (2 * a) - (2 * r1)
eccentricity = c / a

#Heliocentric
transfer_energy = - mu_sun / (r1 + r2) #epsilon_t
v1 = m.sqrt(2 * ((mu_sun / r1) + transfer_energy)) #heliocentric velocity
v_starting_planet = m.sqrt(mu_sun / r1)
v_escape_starting = abs(v1 - v_starting_planet) 

v2 = m.sqrt(2 * ((mu_sun / r2) + transfer_energy))
target_energy = -(mu_sun / r2)
target_velocity = m.sqrt(mu_sun / r2) #v_target

#Departure
v_inf  = v1 - v_starting_planet
escape_energy = (v_inf ** 2) / 2
v0 = m.sqrt(2 * (f.get_mu(starting_planet) / starting_orbital_radius) + escape_energy)

v_starting_park = m.sqrt(f.get_mu(starting_planet) / starting_orbital_radius)
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
    print("Total velocity change:", delta_v_mission, "km/s")
    f.TOF(a)