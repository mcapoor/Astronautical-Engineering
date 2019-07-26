import math as m
specific_impulse = {'zinc/sulfur':240, 'aluminum/ammonium perchlorate':287, 'hydrazine/nitrogen tetroxide':313, 'ethanol/oxygen':330, 'methane/oxygen':370, 'hydrogen/oxygen':465, 'thermal rockets':900, 'ion rockets':3000, 'solid boosters':269, }
thrust = {'methane/liquid oxygen':

payload_mass #mL
initial_mass #m0
structural_mass #ms
propellant_mass #mp

payload_ratio #lambda

burnout_time #tb
             
burnout_mass #mb

def epsilon(ms=structural_mass, mp=propellant_mass):
    return ms / (mp + ms)

def get_R(lam=payload_ratio):
    return (1 + lam) /  (epsilon() + lam)

u_equivalent = g[body] * specific_impulse[fuel]
delta_u = u_equivalent * m.log((initial_mass / burnout_mass))