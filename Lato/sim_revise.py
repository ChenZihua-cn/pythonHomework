"""
不知道什么东西,输出了个图片
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

# Constants
m = 1.0  # mass of the ball (kg)
L = 1.0  # length of the rope (m), fixed for rigid rope
g = 9.81  # gravitational acceleration (m/s^2)
omega_drive = 1.0  # driving angular frequency (rad/s)
A_drive = 0.1  # driving amplitude (m)

# Differential equations for rigid rope
def lato_lato_rigid_corrected(t, y):
    phi, dphi = y  # angle and angular velocity
    # Driving force: introduce a small oscillation to the anchor point
    drive_phi = A_drive * np.sin(omega_drive * t)  # smooth angular driving
    d2phi = -(g / L) * np.sin(phi + drive_phi)  # Angular acceleration with drive
    return [dphi, d2phi]

# Initial conditions
phi_initial = 0.1  # initial angle (radians)
dphi_initial = 0.0  # initial angular velocity (rad/s)
y0 = [phi_initial, dphi_initial]

# Time span for simulation
t_span = (0, 10)  # 10 seconds
t_eval = np.linspace(t_span[0], t_span[1], 1000)

# Solve the equations
sol = solve_ivp(lato_lato_rigid_corrected, t_span, y0, t_eval=t_eval, method='RK45')

# Extract results
phi = sol.y[0]  # angular displacement
r = L * np.ones_like(phi)  # constant radius for rigid rope

# Convert to Cartesian coordinates for visualization
x = r * np.cos(phi)
y = r * np.sin(phi)

# Plot the results
plt.figure(figsize=(10, 5))

# Radial motion (constant for rigid rope) and angular motion
plt.subplot(1, 2, 1)
plt.plot(sol.t, r, label="Radius (r)")
plt.plot(sol.t, phi, label="Angle (phi)")
plt.xlabel("Time (s)")
plt.ylabel("Radial/Angular Values")
plt.legend()
plt.title("Radial and Angular Motion (Rigid Rope)")

# Trajectory in Cartesian coordinates
plt.subplot(1, 2, 2)
plt.plot(x, y)
plt.xlabel("X (m)")
plt.ylabel("Y (m)")
plt.title("Trajectory in Cartesian Coordinates (Rigid Rope)")

plt.tight_layout()
plt.show()
