#Calculate Hohmann transfer TOF and delta_v
import functions

import math as m

mode = input("Interplanetary or In-Plane transfer? ").lower()
if (mode == 'interplanetary'):
    import interplanetary
    interplanetary.interplanetary()
elif (mode == 'in-plane'):
    import in_plane
    in_plane.in_plane()

