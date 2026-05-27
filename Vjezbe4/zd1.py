import numpy as np
import matplotlib.pyplot as plt


def gbanje(q, m, E, B, v0, r0, t_max, dt):
    N = int(t_max / dt)
    r = np.zeros((N, 3))
    v = np.zeros((N, 3))
    r[0] = r0
    v[0] = v0
    for i in range(1, N):
        vx, vy, vz = v[i-1]
        v_cross_B = np.array([vy * B[2], -vx * B[2], 0.0])
        a = (q / m) * (E + v_cross_B)
        v[i] = v[i-1] + a * dt
        r[i] = r[i-1] + v[i] * dt
    return r
m = 1.0
e = 1.0
v0 = np.array([1.0, 0.5, 0.2]) #sve tri komponente su razlicite 
r0 = np.array([0.0, 0.0, 0.0]) #gledamo iz ishodista

t_max = 50.0
dt = 0.01

#B=const
E_0 = np.array([0.0, 0.0, 0.0])
B_const = np.array([0.0, 0.0, 1.0])

r_e_B = gbanje(-e, m, E_0, B_const, v0, r0, t_max, dt)
r_p_B = gbanje(e, m, E_0, B_const, v0, r0, t_max, dt)

#E || B
E_paralelno = np.array([0.0, 0.0, 0.1])
r_e_EB1 = gbanje(-e, m, E_paralelno, B_const, v0, r0, t_max, dt)
r_p_EB1 = gbanje(e, m, E_paralelno, B_const, v0, r0, t_max, dt)

#E okomito na B
E_okomito = np.array([0.2, 0.0, 0.0])
r_e_EB2 = gbanje(-e, m, E_okomito, B_const, v0, r0, t_max, dt)
r_p_EB2 = gbanje(e, m, E_okomito, B_const, v0, r0, t_max, dt)

#crtanje grafa
fig = plt.figure(figsize=(18, 5))
#B=const.
ax1 = fig.add_subplot(131, projection='3d')
ax1.plot(r_e_B[:, 0],r_e_B[:, 1],r_e_B[:, 2],label='Elektron (e-)',color='blue')
ax1.plot(r_p_B[:, 0],r_p_B[:, 1],r_p_B[:, 2],label='Pozitron (e+)',color='red')
ax1.set_title("Samo magnetsko polje B=(0,0,1)")
ax1.set_xlabel('X')
ax1.set_ylabel('Y')
ax1.set_zlabel('Z')
ax1.legend()
#E || B
ax2 = fig.add_subplot(132, projection='3d')
ax2.plot(r_e_EB1[:, 0],r_e_EB1[:, 1],r_e_EB1[:, 2],label='Elektron (e-)',color='blue')
ax2.plot(r_p_EB1[:, 0],r_p_EB1[:, 1],r_p_EB1[:, 2],label='Pozitron (e+)',color='red')
ax2.set_title("E || ($\parallel$) B: E=(0,0,0.1), B=(0,0,1)")
ax2.set_xlabel('X')
ax2.set_ylabel('Y')
ax2.set_zlabel('Z')
ax2.legend()
#E okomito na B
ax3 = fig.add_subplot(133, projection='3d')
ax3.plot(r_e_EB2[:, 0],r_e_EB2[:, 1],r_e_EB2[:, 2],label='Elektron (e-)',color='blue')
ax3.plot(r_p_EB2[:, 0],r_p_EB2[:, 1],r_p_EB2[:, 2],color='red',label='Pozitron (e+)')
ax3.set_title("E ($\perp$) B: E=(0.2,0,0), B=(0,0,1)")
ax3.set_xlabel('X')
ax3.set_ylabel('Y')
ax3.set_zlabel('Z')
ax3.legend()

plt.tight_layout()
plt.show()