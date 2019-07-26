#Calculate Hohmann transfer TOF and delta_v

mode = input("Are we already in orbit? ").lower()
if (mode == 'yes' or mode == 'y'):
    mode = input("Interplanetary or In-Plane transfer? ").lower()
    if (mode == 'interplanetary' or mode == '0'):
        import interplanetary
        interplanetary.interplanetary()
    elif (mode == 'in-plane' or mode == 'inplane' or mode == '1'):
        import in_plane
        in_plane.in_plane()
elif (mode == 'no' or mode == 'n'):
    import launch


