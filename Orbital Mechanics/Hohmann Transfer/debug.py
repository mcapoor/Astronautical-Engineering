import interplanetary as i
import functions
import math as m

print("planet =", i.starting_planet)

print("r1 =", i.r1)
print("r2 =", i.r2)
print("a =", (i.r1 + i.r2) / 2)

print("mu_sun =", i.mu_sun)
print("epsilon_t =", i.transfer_energy)

print("SOI Origin:", i.origin_sphere_of_influence)
print("SOI Target:", i.target_sphere_of_influence)

#heliocentric
print("epsilon_transfer_orbit =", i.transfer_energy)
print("epsilon_target =", i.energy_target)
print("v_origin_planet =", i.v_starting_planet)
print("v_target =", i.target_velocity)
print("v1 =", i.v1)
print("v2 =", i.v2)
print("v_inf_origin =", i.v_inf)
print("v_inf_target =", i.v_inf_target)

#departure
print("epsilon_inf_origin =", i.escape_energy)
print("v_burnout_origin =", i.escape_energy)
print("v_park_origin =", i.v_starting_park)
print("delta_v_boost =", i.delta_v_boost)

#arrival
print("epsilon_inf_target =", i.energy_target)
print("v_burnout_target =", i.v_hyperbolic)
print("v_park_target =", i.v_target_park)
print("delta_v_retro =", i.delta_v_retro)

print("delta_v_mission =", i.delta_v_mission)

print("eccentricity =", i.eccentricity)

