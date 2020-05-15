def angle(h, min):
    # h - hours, min - minutes
    if h >= 12: h = h - 12
    # angle between arrows, because 1 hour does 1 sector of 30 degrees
    # and 1 minute does 1\6 sector or 6 degrees,
    # the hour arrow also does microsteps depending of minute arrow position for 0,5 degree for minute
    a=30.0*h-5.5*min
    # to avoid minus in angle
    a=abs(a)
    # to normalize angle to lesser value
    while a>180: a=a-180
    return a

print(angle(11,59))
