import numpy as np
import matplotlib.pyplot as plt
from projectile import Projectile

dt_lista = [0.5, 0.1, 0.05, 0.01, 0.001]
rez = {}

for d in dt_lista:
    p = Projectile(theta=45, v0=30, x=0, y=0, dt=d, r=0.05, m=0.5)
    p.Euler()
    rez[d] = (p.x_p, p.y_p)

plt.figure()

for d, putanja in rez.items():
    x, y = putanja
    plt.plot(x, y, label=f'dt = {d}s')

plt.axhline(0, color='black', lw=1)
plt.title("Utjecaj koraka dt na preciznost (Eulerova metoda)")
plt.xlabel("Udaljenost/m")
plt.ylabel("Visina/m")
plt.legend(loc='upper right')
plt.grid(True)
plt.show()