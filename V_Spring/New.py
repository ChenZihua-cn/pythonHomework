import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

# Parameters
m = 1.0  # Mass in kg
k = 10.0  # Spring constant in N/m
theta = np.pi / 4  # Angle of springs in radians
F_max = 10.0  # Maximum applied force
time_end = 10  # Total time for simulation
steps = 1000  # Number of time steps

# Equations of motion
def model(t, y):
    x, v = y
    F_applied = F_max * np.sin(0.5 * np.pi * t)  # Example sinusoidal force
    
    # Spring forces (simplified for symmetry)
    F_spring = 2 * k * x * np.cos(theta)
    
    # Equation of motion: m * dv/dt = -F_spring + F_applied
    dxdt = v
    dvdt = (-F_spring + F_applied) / m
    return [dxdt, dvdt]

# Initial conditions: [x0, v0]
y0 = [0.0, 0.0]

# Time vector
t_span = (0, time_end)
t_eval = np.linspace(0, time_end, steps)

# Solve the ODE
sol = solve_ivp(model, t_span, y0, t_eval=t_eval)

# Plotting the results
plt.plot(sol.t, sol.y[0], label="Displacement")
plt.xlabel("Time [s]")
plt.ylabel("Displacement [m]")
plt.title("Mass-Spring System with V-shaped Springs")
plt.legend()
plt.show()
