"""
Traceback (most recent call last):
  File "d:\Code\PY\Lato\simulated2.py", line 45, in <module>
    ani = animation.FuncAnimation(fig, update, frames=len(t), init_func=init, blit=True, interval=30)
                                                          ^
NameError: name 't' is not defined
"""

import matplotlib.animation as animation
import matplotlib.pyplot as plt
import numpy as np

# Parameters
g = 9.8  # gravitational acceleration (m/s^2)
L = 1.0  # length of the string (m)
A = 0.1  # amplitude of pivot oscillation (m)
omega = 2.0  # angular frequency of the pivot oscillation (rad/s)
m1, m2 = 0.1, 0.1  # masses of the two balls (kg)
damping = 0.01  # damping factor for energy loss
time_steps = 300  # number of frames for animation
dt = 0.05  # time step size

# Time range for simulation
t_span = (0, 10)  # 10 seconds
t_eval = np.linspace(t_span[0], t_span[1], 1000)  # time points for evaluation

# Create a figure for animation
fig, ax = plt.subplots(figsize=(10, 6))
line, = ax.plot([], [], lw=2, label="Resonance Response")
ax.set_xlim(t_span[0], t_span[1])
ax.set_ylim(-2 * A, 2 * A)  # Set y-limits to visualize oscillation
ax.set_title("Dynamic Resonance in Forced Harmonic Oscillator")
ax.set_xlabel("Time (s)")
ax.set_ylabel("Angular Displacement (theta)")
ax.grid(True)
ax.legend()



# Initialization function for the animation
def init():
    line.set_data([], [])
    return line,

# Update function for the animation
def update(frame):
    current_t = t[:frame]
    current_theta = theta[:frame]
    line.set_data(current_t, current_theta)
    return line,

# Create the animation
ani = animation.FuncAnimation(fig, update, frames=len(t), init_func=init, blit=True, interval=30)

# Display the animation
plt.show()
