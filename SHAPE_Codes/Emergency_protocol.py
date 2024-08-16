
"""
Note: This is a theoretical code, so do not take this too seriously, obviously this is very vague. We do not have access to sensors,
nor do we have an actual trolley to implement the actual code that works, so dont criticize us too much :)
"""

import numpy as np

V_trolley = int(input("the speed of the trolley: ")) #we dont have the actual trolley and actual sensors, so we'll just say it is input
D = int(input("the distance form trolley to the stop ")) #D is measured in meters

Emergency_wheel_initiation = False


if((D <= 1) and (V_trolley) == 0):
    while(V_trolley < 5.56):
        Emergency_wheel_initiation = True
    else:
        Emergency_wheel_initiation = True

    