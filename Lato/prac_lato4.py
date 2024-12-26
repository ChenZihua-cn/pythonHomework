"""
只有一个球看上去可以用的图片
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

# Constants
m =1.0  # mass of the ball (kg)
g = 9.81  # gravitational acceleration (m/s^2)
omega = 2.0  # angular velocity (rad/s)
r_initial = 1.0  # initial radius (m)
phi_initial = 0.1  # initial angle (radians)
dr_initial = 0.0  # initial radial velocity (m/s)
dphi_initial = 0.0  # initial angular velocity (rad/s)

# Differential equations
def lato_lato(t, y):
    r, dr, phi, dphi = y  # unpack the variables
    # Radial and angular equations of motion
    T = m * (omega**2 * r + g * np.sin(phi))  # approximate tension force
    d2r = T * np.cos(phi) / m - omega**2 * r - g * np.sin(phi)
    d2phi = (T * np.sin(phi) - g * np.cos(phi)) / (m * r) - 2 * dr * omega / r
    return [dr, d2r, dphi, d2phi]

# Initial conditions
y0 = [r_initial, dr_initial, phi_initial, dphi_initial]

# Time span for simulation
t_span = (0, 10)  # 10 seconds
t_eval = np.linspace(t_span[0], t_span[1], 1000)

# Solve the equations
sol = solve_ivp(lato_lato, t_span, y0, t_eval=t_eval, method='RK45')

# Extract results
r = sol.y[0]
phi = sol.y[2]

# Convert to Cartesian coordinates for visualization
x = r * np.cos(phi)
y = r * np.sin(phi)

# Plot the results
plt.figure(figsize=(10, 5))

# Radial motion
plt.subplot(1, 2, 1)
plt.plot(sol.t, r, label="Radius (r)")
plt.plot(sol.t, phi, label="Angle (phi)")
plt.xlabel("Time (s)")
plt.ylabel("Radial/Angular Values")
plt.legend()
plt.title("Radial and Angular Motion")

# Trajectory in Cartesian coordinates
plt.subplot(1, 2, 2)
plt.plot(x, y)
plt.xlabel("X (m)")
plt.ylabel("Y (m)")
plt.title("Trajectory in Cartesian Coordinates")

plt.tight_layout()
plt.show()
