from particle import Particle
import numpy as np

import matplotlib.pyplot as plt


delta_t=[0.1,0.075, 0.05,0.025,0.01,0.0075,0.005,0.0025,0.001]

pogreske=[]

def analiticki(v0,theta):
    theta=np.radians(theta)
    g=9.81
    D=v0**2*np.sin(2*theta)/g
    return D

analiticki_D=analiticki(10,60)

for dt in delta_t:
    p=Particle(10,60,0,0)
    p.dt=dt
    numericki_D=p.range()
    rel_pogreska=abs(numericki_D-analiticki_D)/analiticki_D*100
    pogreske.append(rel_pogreska)

plt.plot(delta_t,pogreske,marker='o')
plt.xlabel("Vremenski odmaci (delta t) / s")
plt.ylabel("Relativna pogreška / %")
plt.title("Ovisnost relativne pogrške o odabranom dt")
plt.grid("True")
plt.show()