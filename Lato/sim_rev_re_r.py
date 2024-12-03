import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

# Constants
m = 1.0  # mass of each ball (kg)
L = 1.0  # length of the rigid rope (m)
g = 9.81  # gravitational acceleration (m/s^2)
A_drive = 0.1  # driving amplitude (m)
omega_drive = 2.0  # driving angular frequency (rad/s)

# Differential equations
def lato_lato_rigid(t, y):
    # Unpack variables
    phi1, dphi1, phi2, dphi2 = y
    
    # Driving angle (sinusoidal hand motion)
    drive_phi = A_drive * np.sin(omega_drive * t)
    
    # Forces and accelerations
    d2phi1 = -(g / L) * np.sin(phi1 + drive_phi) + (dphi2 - dphi1) * dphi2 / L
    d2phi2 = -(g / L) * np.sin(phi2 + drive_phi) - (dphi2 - dphi1) * dphi1 / L
    
    return [dphi1, d2phi1, dphi2, d2phi2]

# Initial conditions
phi1_initial = 0.1  # initial angle of ball 1 (radians)
dphi1_initial = 0.0  # initial angular velocity of ball 1
phi2_initial = -0.1  # initial angle of ball 2 (radians)
dphi2_initial = 0.0  # initial angular velocity of ball 2
y0 = [phi1_initial, dphi1_initial, phi2_initial, dphi2_initial]

# Time span for simulation
t_span = (0, 10)  # simulate for 10 seconds
t_eval = np.linspace(t_span[0], t_span[1], 1000)  # time steps for evaluation

# Solve the equations
sol = solve_ivp(lato_lato_rigid, t_span, y0, t_eval=t_eval, method='RK45')

# Extract results
phi1 = sol.y[0]
phi2 = sol.y[2]

# Convert to Cartesian coordinates for both balls
x1 = L * np.sin(phi1)
y1 = -L * np.cos(phi1)
x2 = -L * np.sin(phi2)
y2 = -L * np.cos(phi2)

# Plot the results
plt.figure(figsize=(12, 6))

# Angular motion of the two balls
plt.subplot(1, 2, 1)
plt.plot(sol.t, phi1, label="Ball 1 Angle (phi1)")
plt.plot(sol.t, phi2, label="Ball 2 Angle (phi2)")
plt.xlabel("Time (s)")
plt.ylabel("Angle (radians)")
plt.legend()
plt.title("Angular Motion of Balls (Rigid Rope)")

# Cartesian coordinates (trajectory)
plt.subplot(1, 2, 2)
plt.plot(x1, y1, label="Ball 1")
plt.plot(x2, y2, label="Ball 2")
plt.xlabel("X (m)")
plt.ylabel("Y (m)")
plt.legend()
plt.title("Trajectory in Cartesian Coordinates (Rigid Rope)")

plt.tight_layout()
plt.show()
