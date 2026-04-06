from  particle import Particle

import numpy as np

def analitcki(v0,theta):
    theta=np.radians(theta)
    g=9.81
    D=v0**2*np.sin(2*theta)/g
    return D

test = [
    (10,45),
    (9,90),
    (5,50),
    (70,15)
]

for v0,theta in test:
    p=Particle(v0,theta,0,0)
    numericki=p.range()
    a=analitcki(v0,theta)
    odstupanje=abs(numericki-a)
    rel_odstupanje=odstupanje/a*100
    print(f"v0: {v0} theta: {theta}, analiticki: {a},numericki: {numericki}, odstupanje{odstupanje}, relativno: {rel_odstupanje}%")