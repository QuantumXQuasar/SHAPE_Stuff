"""
Note: This is a theoretical code, so do not take this too seriously, obviously this is very vague. We do not have access to sensors,
nor do we have an actual trolley to implement the actual code that works, so dont criticize us too much :)
"""

import numpy as np

StartBreaks = False
D = int(input("the distance from the stop: ")) #sensors will measure the distance from the stop, since we dont have sensors, we'll present input

dddt = int(input("velue of dd/dt: ")) 
"""
this will be the the derivative of distance over time from the trolley to the stop, this will determine whether the trolley
is moving to the stop or away from the stop 

"""
if (dddt <= 0):
    if(D <= 10):
        StartBreaks = True
    else:
        StartBreaks = False

print(StartBreaks)