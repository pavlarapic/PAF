import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

g = 9.81  # m/s^2
L1_teorijski = 0.120
L2_teorijski = 0.240

kut_deg = np.array([0, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85])
kut_rad = np.radians(kut_deg)

T_120 = np.array([0.8020, 0.8187, 0.8327, 0.8660, 0.8980, 0.9153, 0.9293, 0.9653, 
                  0.9747, 1.0200, 1.0373, 1.1160, 1.1780, 1.2733, 1.4180, 1.6373, 1.9100, 2.5460])

T_240 = np.array([1.0140, 1.0320, 1.0433, 1.0673, 1.0840, 1.1320, 1.1440, 1.1720, 
                  1.1980, 1.2293, 1.2813, 1.3573, 1.4200, 1.5600, 1.7413, 1.9840, 2.4473, 3.1573])
def calc_period(theta_rad,l_duljina):
    return 2*np.pi*np.sqrt(l_duljina/(g*np.cos(theta_rad)))

curvefit120t,curvefit120v = curve_fit(calc_period,kut_rad,T_120)
curvefit240t,curvefit240v = curve_fit(calc_period,kut_rad,T_240)

l_fit_120= curvefit120t[0]
err_l_120=np.sqrt(curvefit120v[0,0])

l_fit_240=curvefit240t[0]
err_l_240=np.sqrt(curvefit120v[0,0])

rel_err_120=np.abs(l_fit_120-L1_teorijski)/L1_teorijski * 100


print(f"Teorijska duljina 1: {L1_teorijski:.5f} m")
print(f"Izračunata duljina l: {l_fit_120:.5f} greska {err_l_120:.5f} m")
print(f"Relativna pogreška mjerenja: {rel_err_120:.4f} %")

print(f"Teorijska duljina 2: {L2_teorijski:.3f} m")
print(f"Izračunata duljina l: {l_fit_240:.4f} greska {err_l_240:.4f} m")

kut_glatko_deg=np.linspace(0,85,200)
kut_glatko_rad=np.radians(kut_glatko_deg)

plt.figure(figsize=(10, 6))

plt.scatter(kut_deg, T_120, color='red', label='mjerenja')
plt.plot(kut_glatko_deg, calc_period(kut_glatko_rad,L1_teorijski), '--', color='orange', label='Teorija (120 mm)')
plt.plot(kut_glatko_deg, calc_period(kut_glatko_rad, l_fit_120), color='red', label=f'Regresija l={l_fit_120:.4f}m')

plt.scatter(kut_deg, T_240, color='blue', label='mjerenja')
plt.plot(kut_glatko_deg, calc_period(kut_glatko_rad, L2_teorijski), '--', color='cyan', label='Teorija (240 mm)')
plt.plot(kut_glatko_deg, calc_period(kut_glatko_rad, l_fit_240), color='blue', label=f'Regresija l={l_fit_240:.4f}m')

plt.xlabel('Kut otklona/rad')
plt.ylabel('Period titranja $T [s]$')
plt.title('Ovisnost perioda titranja o kutu naklona')
plt.grid(True)
plt.legend(loc='upper left')
plt.tight_layout()
plt.show()
