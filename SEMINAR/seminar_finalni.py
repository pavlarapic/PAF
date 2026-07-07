import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from collections import deque

L1, L2 = 1.0, 1.0
m1, m2 = 1.0, 1.0
g = 9.81

def so2_matrix(theta):
    return np.array([[np.cos(theta), -np.sin(theta)],
                     [np.sin(theta),  np.cos(theta)]])

def equations_of_motion(y):
    t1, t2, w1, w2 = y
    delta = t1 - t2
    
    M11 = (m1 + m2) * L1**2
    M12 = m2 * L1 * L2 * np.cos(delta)
    M21 = M12
    M22 = m2 * L2**2
    M = np.array([[M11, M12], 
                  [M21, M22]])
    
    C1 = -m2 * L1 * L2 * w2**2 * np.sin(delta) - (m1 + m2) * g * L1 * np.sin(t1)
    C2 =  m2 * L1 * L2 * w1**2 * np.sin(delta) - m2 * g * L2 * np.sin(t2)
    C = np.array([C1, C2])
    
    accel = np.linalg.solve(M, C)
    
    return np.array([w1, w2, accel[0], accel[1]])

def rk4_step(y, dt):
    k1 = equations_of_motion(y)
    k2 = equations_of_motion(y + 0.5 * dt * k1)
    k3 = equations_of_motion(y + 0.5 * dt * k2)
    k4 = equations_of_motion(y + dt * k3)
    
    return y + (dt / 6.0) * (k1 + 2*k2 + 2*k3 + k4)

y = np.array([np.pi / 2, np.pi / 2, 0.0, 0.0])

t_max = 15.0
dt = 0.02
num_steps = int(t_max / dt)

x1, y1 = [], []
x2, y2 = [], []

for _ in range(num_steps):
    t1, t2 = y[0], y[1]
    
    R1 = so2_matrix(t1)
    R2 = so2_matrix(t2)
    
    p1 = R1 @ np.array([0, -L1])
    p2 = p1 + R2 @ np.array([0, -L2])
    
    x1.append(p1[0])
    y1.append(p1[1])
    x2.append(p2[0])
    y2.append(p2[1])
    
    y = rk4_step(y, dt)

fig, ax = plt.subplots(figsize=(7, 7))
ax.set_xlim(-2.2, 2.2)
ax.set_ylim(-2.2, 2.2)
ax.set_aspect('equal')
ax.grid(True, linestyle='--', alpha=0.6)
ax.set_title("Simulacija dvostrukog njihala", fontsize=12)
ax.set_xlabel("x os")
ax.set_ylabel("y os")

line, = ax.plot([], [], 'o-', lw=3, color='#1f77b4', markersize=8, markerfacecolor='#ff7f0e')
trace, = ax.plot([], [], '-', lw=1.5, color='#d62728', alpha=0.6)

x2_trace = deque(maxlen=120)
y2_trace = deque(maxlen=120)

def init():
    line.set_data([], [])
    trace.set_data([], [])
    return line, trace

def animate(i):
    thisx = [0, x1[i], x2[i]]
    thisy = [0, y1[i], y2[i]]
    
    x2_trace.append(x2[i])
    y2_trace.append(y2[i])
    
    line.set_data(thisx, thisy)
    trace.set_data(list(x2_trace), list(y2_trace))
    return line, trace

ani = animation.FuncAnimation(fig, animate, frames=num_steps,
                              init_func=init, blit=True, interval=20, repeat=True)
ani.save("pr_dvostruko_njihalo.mp4",writer="ffmpeg",fps=50)
plt.show()