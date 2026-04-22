import numpy as np
import matplotlib.pyplot as plt
from projectile import Projectile

p=Projectile(45,10,0,0,0.01,0.07,0.25,1.225,9.81,0.47)

euler_x,euler_y = p.Euler()
rk4_x,rk4_y=p.Runge_Kutta_4()

plt.figure()
plt.plot(euler_x,euler_y,'r--',label='Eulerova metoda za dt=0.01s')
plt.plot(rk4_x,rk4_y,'b',label='Runge-Kutta metoda 4. reda za dt=0.01s')
plt.xlabel("Udaljenost/m")
plt.ylabel("Visina/m")
plt.axhline(0,color='black',lw=1)
plt.grid(True)
plt.legend(loc='lower right')
plt.show()