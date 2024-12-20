"""
生成了一个图片,但是并没有考虑绳子弹性,并且只有一个球
微分方程是（角度的二阶导）+(固有频率^2) * (角度) = (A * omega^2 / L) * sin(omega * t)
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

# Parameters
g = 9.81  # gravity (m/s^2)
L = 1.0   # length of pendulum (m)
A = 0.1   # amplitude of driving force (m)
omega_0 = np.sqrt(g / L)  # natural frequency (rad/s)
omega = omega_0  # driving frequency close to natural frequency (resonance)

# Differential equation: d^2(theta)/dt^2 + omega_0^2 * theta = (A * omega^2 / L) * sin(omega * t)
def forced_harmonic_oscillator(t, y):
    theta, dtheta_dt = y
    d2theta_dt2 = -omega_0**2 * theta + (A * omega**2 / L) * np.sin(omega * t)
    return [dtheta_dt, d2theta_dt2]

# Initial conditions: [theta(0), dtheta/dt(0)]
y0 = [0.0, 0.0]

# Time range for simulation
t_span = (0, 10)  # 10 seconds
t_eval = np.linspace(t_span[0], t_span[1], 1000)  # time points for evaluation

# Solve the differential equation
solution = solve_ivp(forced_harmonic_oscillator, t_span, y0, t_eval=t_eval)

# Extract results
t = solution.t
theta = solution.y[0]

# Plot the results
plt.figure(figsize=(10, 6))
plt.plot(t, theta, label="Resonance Response")
plt.title("Resonance in Forced Harmonic Oscillator")
plt.xlabel("Time (s)")
plt.ylabel("Angular Displacement (theta)")
plt.grid(True)
plt.legend()
plt.show()
