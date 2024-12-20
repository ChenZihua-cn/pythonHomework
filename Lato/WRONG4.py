"""
IndexError: list index out of range
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Parameters
g = 9.8  # gravitational acceleration (m/s^2)
L = 1.0  # length of the string (m)
A = 0.1  # amplitude of pivot oscillation (m)
omega = 2.0  # angular frequency of the pivot oscillation (rad/s)
m1, m2 = 0.1, 0.1  # masses of the two balls (kg)
damping = 0.01  # damping factor for energy loss
time_steps = 300  # number of frames for animation
dt = 0.05  # time step size

# Time array
t = np.linspace(0, time_steps * dt, time_steps)

# Initial conditions: angles and angular velocities
theta1, theta2 = np.pi / 4, -np.pi / 4  # initial angles (radians)
omega1, omega2 = 0.0, 0.0  # initial angular velocities

# Function to compute dynamics at each step
def compute_dynamics(theta1, theta2, omega1, omega2, t):
    theta1_list, theta2_list = [theta1], [theta2]
    x1_list, y1_list, x2_list, y2_list = [], [], [], []
    omega1_list, omega2_list = [omega1], [omega2]
    
    for i in range(1, len(t)):
        # Pivot oscillation
        pivot_x = A * np.sin(omega * t[i])

        # Angular accelerations (simplified pendulum dynamics)
        alpha1 = -(g / L) * np.sin(theta1) - damping * omega1
        alpha2 = -(g / L) * np.sin(theta2) - damping * omega2
        
        # Update angular velocities
        omega1 += alpha1 * dt
        omega2 += alpha2 * dt

        # Update angles
        theta1 += omega1 * dt
        theta2 += omega2 * dt

        # Ball positions based on updated angles
        x1 = pivot_x + L * np.sin(theta1)
        y1 = -L * np.cos(theta1)
        x2 = pivot_x + L * np.sin(theta2)
        y2 = -L * np.cos(theta2)

        # Store values
        theta1_list.append(theta1)
        theta2_list.append(theta2)
        omega1_list.append(omega1)
        omega2_list.append(omega2)
        x1_list.append(x1)
        y1_list.append(y1)
        x2_list.append(x2)
        y2_list.append(y2)

    return x1_list, y1_list, x2_list, y2_list, pivot_x

# Compute dynamics
x1, y1, x2, y2, pivot_x = compute_dynamics(theta1, theta2, omega1, omega2, t)

# Animation setup
fig, ax = plt.subplots(figsize=(6, 6))
ax.set_xlim(-L - A, L + A)
ax.set_ylim(-L - 0.2, 0.2)
ax.set_aspect('equal')
ax.axis('off')

# Objects to animate
pivot, = ax.plot([], [], 'ko', markersize=8)  # Pivot point
line1, = ax.plot([], [], 'r-', lw=2)  # String for ball 1
ball1, = ax.plot([], [], 'ro', markersize=10)  # Ball 1
line2, = ax.plot([], [], 'b-', lw=2)  # String for ball 2
ball2, = ax.plot([], [], 'bo', markersize=10)  # Ball 2

# Initialize function
def init():
    pivot.set_data([], [])
    line1.set_data([], [])
    ball1.set_data([], [])
    line2.set_data([], [])
    ball2.set_data([], [])
    return pivot, line1, ball1, line2, ball2

def update(frame):
    # Update the pivot position
    pivot.set_data([pivot_x], [0])

    # Update ball 1 position
    line1.set_data([pivot_x, x1[frame]], [0, y1[frame]])
    ball1.set_data([x1[frame]], [y1[frame]])

    # Update ball 2 position
    line2.set_data([pivot_x, x2[frame]], [0, y2[frame]])
    ball2.set_data([x2[frame]], [y2[frame]])

    print(f"Frame {frame}, x1: {x1[frame]}, y1: {y1[frame]}")

    return pivot, line1, ball1, line2, ball2



# Create animation
ani = FuncAnimation(fig, update, frames=len(t), init_func=init, blit=True)

# Save or display the animation
ani.save("lato_lato_simulation.gif", writer="pillow", fps=30)
plt.show()
