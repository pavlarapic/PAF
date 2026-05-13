from arithm import arithm
#lijeno mi je opet raditi isti kod 
import numpy as np
M=[0.052,0.124,0.168,0.236,0.284,0.336]
phi=[0.1745,0.3491,0.5236,0.6981,0.8727,1.0472] 

x=np.array(phi)
y=np.array(M)

xy=x*y
x_sq=x**2
y_sq=y**2

avg_xy=arithm(xy).aritm_sredina()
avg_x2=arithm(x_sq).aritm_sredina()
avg_y2=arithm(y_sq).aritm_sredina()
a=avg_xy/avg_x2
n=len(x)
sigma_a=np.sqrt((1/n)*(avg_y2/avg_x2-a**2))
print(f"Modul torzije Dt iznosi: {a:.5f} Nm/rad")
print(f"Pogreška modula torzije iznosi: {sigma_a:.5f}")

import matplotlib.pyplot as plt
plt.scatter(x,y,color='red',label='Mjerenja')
plt.plot(x,a*x,label=f'Regresija: M={a:.5f}*phi')
plt.xlabel('phi/rad]')
plt.ylabel('M/Nm')
plt.legend()
plt.grid(True)
plt.show()