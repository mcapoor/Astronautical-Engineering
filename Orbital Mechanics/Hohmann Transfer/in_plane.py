import functions
import math as m

def in_plane():
    planet = input("Which body are we starting from? ")
    if (planet == 'e'):
        planet = 'earth'

    mu = functions.get_mu(planet)

    radii1 = functions.get_altitude1(planet)
    altitude1 = radii1[0]
    r1 = radii1[1]

    radii2 = functions.get_altitude2(planet)
    altitude2 = radii2[0]
    r2 = radii2[1]
        
    epsilon = (mu / (r1 + r2))

    a = (r1 + r2) / 2
        
    v1 = m.sqrt(2 * ((mu / r1) + epsilon))
    vcs1 = m.sqrt(mu / r1)
    delta_v1 = v1 - vcs1

    v2 = m.sqrt(2 * ((mu / r2) + epsilon))
    vcs2 = m.sqrt(mu / r2)
    delta_v2 = vcs2 - v2

    total_velocity_change = delta_v1 + delta_v2

    print()
    print("Total Energy:", epsilon, "joules")
    print("Orbital Velocity:", vcs2, "km/s")
    print("The total change in velocity required to move from", altitude1, "km to", altitude2, "km is:", total_velocity_change, "km/s")
    functions.TOF(a)
