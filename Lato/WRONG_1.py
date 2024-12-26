"""
未知错误,成为复摆
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from scipy.integrate import solve_ivp

# Constants
g = 9.81  # gravitational acceleration (m/s^2)
L = 1.0   # length of each string (m)
m = 1.0   # mass of each ball (kg)
A = 0.1   # amplitude of vertical oscillation of the pivot (m)
r_ball = 0.05  # radius of each ball (m)
omega_p = 2.0  # angular frequency of the pivot's oscillation (rad/s)
e = 1.0   # coefficient of restitution (elastic collision)


# Equations of motion
def equations(t, y):
    theta1, z1, theta2, z2 = y
    dtheta1 = z1
    dtheta2 = z2
    dz1 = -(g/L) * np.sin(theta1) - (A * omega_p**2 / L) * np.cos(omega_p * t) * np.cos(theta1)
    dz2 = -(g/L) * np.sin(theta2) - (A * omega_p**2 / L) * np.cos(omega_p * t) * np.cos(theta2)
    return [dtheta1, dz1, dtheta2, dz2]

# Collision detection and response
def handle_collision(y):
    theta1, z1, theta2, z2 = y
    x1, y1 = L * np.sin(theta1), -L * np.cos(theta1)
    x2, y2 = L * np.sin(theta2), -L * np.cos(theta2)
    distance = np.sqrt((x2 - x1)**2 + (y2 - y1)**2)
    if distance < 2 * r_ball:  # collision detected
        v1 = L * z1 * np.cos(theta1)
        v2 = L * z2 * np.cos(theta2)
        v1_new = (v1 * (m - m) + 2 * m * v2) / (m + m)
        v2_new = (v2 * (m - m) + 2 * m * v1) / (m + m)
        z1 = v1_new / (L * np.cos(theta1))
        z2 = v2_new / (L * np.cos(theta2))
    return [theta1, z1, theta2, z2]

# Initial conditions
theta1_initial = 0.1  # initial angle of ball 1 (radians)
theta2_initial = -0.1 # initial angle of ball 2 (radians)
z1_initial = 0.0      # initial angular velocity of ball 1 (rad/s)
z2_initial = 0.0      # initial angular velocity of ball 2 (rad/s)
y0 = [theta1_initial, z1_initial, theta2_initial, z2_initial]

# Time span
t_span = (0, 10)
t_eval = np.linspace(t_span[0], t_span[1], 1000)

# Solve the equations
sol = solve_ivp(equations, t_span, y0, t_eval=t_eval, method='RK45')

# Extract results
theta1 = sol.y[0]
theta2 = sol.y[2]

# Convert to Cartesian coordinates for animation
x1 = L * np.sin(theta1)
y1 = -L * np.cos(theta1)
x2 = L * np.sin(theta2)
y2 = -L * np.cos(theta2)

# Animation
fig, ax = plt.subplots()
ax.set_xlim(-2*L, 2*L)
ax.set_ylim(-2*L, 2*L)
line, = ax.plot([], [], 'o-', lw=2)

def init():
    line.set_data([], [])
    return line,

def update(frame):
    thisx = [0, x1[frame], x2[frame]]
    thisy = [A * np.cos(omega_p * t_eval[frame]), y1[frame] + A * np.cos(omega_p * t_eval[frame]), y2[frame] + A * np.cos(omega_p * t_eval[frame])]
    line.set_data(thisx, thisy)
    return line,

ani = FuncAnimation(fig, update, frames=len(t_eval), init_func=init, blit=True)
plt.show()
