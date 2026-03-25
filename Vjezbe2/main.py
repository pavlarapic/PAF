from particle import Particle
import numpy as np

v0 = 10
theta = 45

p = Particle(v0,theta,0,0)

numericki = p.range()

g = 9.81

analiticki = (v0**2 *np.sin(2*np.radians(theta))) / g

print(f"Numericki {numericki}")
print(f"Analitcki {analiticki}")
print(f"Odstupanje{abs(numericki-analiticki)}")

p.plot_trajectory()
p.__move()