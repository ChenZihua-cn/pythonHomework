import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Parameters
m = 1.0  # Mass (kg)
k = 10.0  # Spring constant (N/m)
L0 = 1.0  # Natural length of springs (m)
g = 9.8  # Gravity (m/s^2)
F0 = 1.0  # External force amplitude (N)
omega = 1.0  # Frequency of external force (rad/s)
t_max = 20  # Simulation time (s)
dt = 0.01  # Time step (s)

# Initial Conditions
x0, y0 = 0.0, -1.0  # Initial position
vx0, vy0 = 0.0, 0.0  # Initial velocities

# Time array
t = np.arange(0, t_max, dt)

# Equations of Motion (Numerical Integration)
def equations_of_motion(state, t):
    x, y, vx, vy = state
    # Lengths of the two springs
    L1 = np.sqrt((x + 1.0)**2 + (y + L0)**2)
    L2 = np.sqrt((x - 1.0)**2 + (y + L0)**2)
    
    # Avoid division by zero
    if L1 == 0:
        L1 = 1e-6
    if L2 == 0:
        L2 = 1e-6
    
    # Forces from the two springs
    Fx_spring = (-k * (L1 - L0) * ((x + 1.0) / L1) - k * (L2 - L0) * ((x - 1.0) / L2))
    Fy_spring = (-k * (L1 - L0) * ((y + L0) / L1) - k * (L2 - L0) * ((y + L0) / L2))

    # External force
    F_ext = F0 * np.cos(omega * t)  # External force in x-direction

    # Accelerations
    ax = (Fx_spring + F_ext) / m
    ay = (Fy_spring - m * g) / m
    
    return [vx, vy, ax, ay]

# Numerical Integration (Runge-Kutta method)
def solve_ode():
    from scipy.integrate import odeint
    initial_state = [x0, y0, vx0, vy0]
    sol = odeint(equations_of_motion, initial_state, t, atol=1e-8, rtol=1e-6)
    return sol[:, 0], sol[:, 1]

# Solve equations
x, y = solve_ode()

# Visualization
fig, ax = plt.subplots()
ax.plot(t, x, label='X-Position')
ax.plot(t, y, label='Y-Position')
ax.set_xlabel('Time (s)')
ax.set_ylabel('Displacement (m)')
ax.legend()
ax.grid(True)
plt.title('Displacement vs Time for V-Spring System')
plt.show()
