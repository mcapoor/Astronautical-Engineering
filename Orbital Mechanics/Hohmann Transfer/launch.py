import math as m
import functions as f

planet = input("Which planet are we launching from?")

escape_velocity = m.sqrt((2 * f.get_mu(planet) / f.body_radius[planet]))
print("Escape Velocity:", escape_velocity, "km/s")

#NOT COVERED: WILL NEED TO RESEARCH INDEPENDENTLY 