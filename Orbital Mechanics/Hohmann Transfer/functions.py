import math as m

body_mu = {'sun':132712000000, 'mercury':22032, 'venus':324860, 'earth':398600,'moon':1, 'mars':42828, 'jupiter':126687000, 'saturn':37931000, 'uranus':5794000, 'neptune':6835100}
body_radius = {'sun':695700, 'mercury':2439.5, 'venus':6052, 'earth':6378, 'moon':1, 'mars':3396, 'jupiter':71492, 'saturn':60268, 'uranus':25559, 'neptune':24764}
orbital_radius = {'sun':1, 'mercury':57900000, 'venus':108100000, 'earth':149500000, 'moon':1, 'mars':227800000, 'jupiter':778000000, 'saturn':1426000000, 'uranus':2868000000, 'neptune':4494000000}
body_mass = {'sun':333432, 'mercury':0.056, 'venus':0.817, 'earth':1, 'moon':1, 'mars':0.108, 'jupiter':318, 'saturn':95.2, 'uranus':14.6, 'neptune':17.3}

def get_altitude1(planet):
    altitude1 = float(input("Altitude of starting orbit (km): "))

    r1 = altitude1 + body_radius[planet]

    return altitude1, r1

def get_altitude2(planet):
    altitude2 = float(input("Altitude of target orbit (km): "))
    r2 = altitude2 + body_radius[planet]

    return altitude2, r2

def get_orbital_radius(planet):
    r_orbit = orbital_radius[planet] + body_radius[planet]
    return r_orbit

def get_mu(planet):
    if planet in body_mu.keys():
        mu = body_mu[planet]
    else:
        print("Error: the gravitational parameter of ", planet, "is not known.")
        mu = input("Please specify mu: ")

    return mu

def get_input():
    starting_planet = input("Which body are we starting from? ")
    if (starting_planet == 'em'):
        starting_planet = 'earth'
        starting_orbital_radius = 6878
        target_planet = 'mars'
        target_orbital_radius = 3896
    else:
        starting_orbital_radius = float(input("What is the initial altitude of the parking orbit? ")) + body_radius[starting_planet]

        target_planet = input("Which body are we going to? ")
        target_orbital_radius = float(input("What is the altitude of the parking orbit on the target planet? ")) + body_radius[target_planet] #rpt

    return starting_planet, starting_orbital_radius, target_planet, target_orbital_radius

def TOF(a):
    mu = get_mu('sun')
    TOF_sec = m.pi * m.sqrt((a ** 3)/ mu)
    if (TOF_sec > 86400):
        TOF_simp = TOF_sec / 86400
        print("The total time necessary to complete this maneuver is:", TOF_simp, "days")
    elif (TOF_sec > 3600):
        TOF_simp = TOF_sec / 3600
        print("The total time necessary to complete this maneuver is:", TOF_simp, "hours")
    elif (TOF_sec > 60):
        TOF_simp = TOF_sec / 60
        print("The total time necessary to complete this maneuver is:", TOF_simp, "minutes")
    else:
        print("The total time necessary to complete this maneuver is:", TOF_sec, "seconds")

