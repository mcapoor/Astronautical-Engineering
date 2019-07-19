import functions
import math as m

def get_planets():
    planet1 = input("Which body are we starting from? ")
    rp0 = float(input("What is the initial altitude of the parking radius? "))
    planet2 = input("Which body are we going to? ")
    rp1 = float(input("What is the altitude of the parking orbit on the target planet? "))

    return planet1, planet2, rp0, rp1

def get_epsilon(planet):
    mu = functions.get_mu(planet)
    epsilon = - mu / (r1 + r2)
    return epsilon
    
planet = get_planets()
planet1 = planet[0]
planet2 = planet[1]
origin_parking_radius = planet[2]
target_parking_radius = planet[3]

r1 = functions.get_orbital_radius(planet1)
r2 = functions.get_orbital_radius(planet2)
a = (r1 + r2) / 2

mu_sun = functions.get_mu('sun')
epsilon_t = get_epsilon('sun')

def transfer():
    #heliocentric
    a = (r1 + r2) / 2
    epsilon_origin = - (mu_sun - (2 * functions.body_radius[planet1]))
    epsilon_transfer_orbit = - (mu_sun / (2 * a))
    epsilon_target = (mu_sun / (2 * functions.body_radius[planet2]))
    v_origin_planet = m.sqrt(mu_sun / r1)
    v_target = m.sqrt(2 * ((mu_sun / r2) + epsilon_target))
    v1 = m.sqrt(2 * ((mu_sun / r1) + epsilon_t))
    v2 = m.sqrt(mu_sun / r1)
    v_inf_origin = abs(v_target - v2)
    v_inf_target = abs(v_target - v2)
   
    #departure
    epsilon_inf_origin = (v_inf_origin ** 2) / 2
    v_burnout_origin = m.sqrt(2 * ((functions.get_mu(planet1) / origin_parking_radius) + epsilon_inf_origin))
    v_park_origin = m.sqrt(functions.get_mu(planet1) / origin_parking_radius)
    delta_v_boost = abs(v_burnout_origin - v_park_origin)

    #arrival
    epsilon_inf_target = (v_inf_target ** 2) / 2
    v_burnout_target = m.sqrt(2 * ((functions.get_mu(planet2) + epsilon_inf_target)))
    v_park_target = m.sqrt((functions.get_mu(planet2) / target_parking_radius) + epsilon_target)
    delta_v_retro = abs(v_park_target - v_burnout_target)

    delta_v_mission = delta_v_boost + delta_v_retro


    if (v_target > v2):
        print()
        print("1) The craft will approach", planet2, "from the front")
    else:
        print()
        print("1) The craft will approach", planet2, "from behind")    

    target_circular_velocity = m.sqrt(functions.get_mu(planet2) / functions.body_radius[planet2])

    arrival_angular_momentum = functions.body_radius[planet2] * v_park_target
    eccentricity = m.sqrt(1 + (2 * epsilon_inf_target * arrival_angular_momentum)/(functions.get_mu(planet2) ** 2))  

    print("2) The eccentricity of the target oribt is:", eccentricity)

    if (eccentricity == 0):
        print("3) The arrival orbit is circular ")
    elif (eccentricity > 0 and eccentricity < 1):
        print("3) The arrival orbit is elliptical ")
    elif (eccentricity == 1):
        print("3) The arrival orbit is parabolic ")
    else:
        print("3) The arrival orbit is hyperbolic ")

    if (eccentricity != 0):
        delta_v_circular = target_circular_velocity - v_park_target
        print("4) The required velocity change to make the orbit circular is:", delta_v_circular/1000, "km/s")
   
    print("5) Total velocity change of the mission is:", (delta_v_mission + delta_v_circular)/1000, "km/s")

def interplanetary():
    transfer()
    functions.TOF(a, '6)')
