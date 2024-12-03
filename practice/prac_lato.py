import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Parameters for the system
length = 1.0           # Length of the strings (meters)
mass = 0.1             # Mass of each ball (kg)
g = 9.81               # Gravitational acceleration (m/s^2)
pivot_amp = 0.2        # Amplitude of the pivot oscillation (meters)
pivot_freq = 2.0       # Frequency of the pivot oscillation (Hz)
time_step = 0.02       # Time step for the simulation

# Initial angles (from the vertical) and angular velocities of the pendulums
theta1 = np.radians(10)
theta2 = np.radians(-10)
omega1 = 0.0
omega2 = 0.0

# Function to compute the pivot's vertical oscillation
def pivot_position(t):
    return pivot_amp * np.sin(2 * np.pi * pivot_freq * t)

# Differential equations for the pendulum system with moving pivot
def derivatives(t, theta1, theta2, omega1, omega2):
    pivot_y = pivot_position(t)
    
    # Acceleration terms for the two pendulums (simplified)
    alpha1 = (-g / length) * np.sin(theta1) - pivot_y * np.cos(theta1)
    alpha2 = (-g / length) * np.sin(theta2) - pivot_y * np.cos(theta2)
    
    return omega1, omega2, alpha1, alpha2

# Integrate the equations of motion using Euler's method
def update_positions(t, theta1, theta2, omega1, omega2):
    omega1_new, omega2_new, alpha1, alpha2 = derivatives(t, theta1, theta2, omega1, omega2)
    omega1 += alpha1 * time_step
    omega2 += alpha2 * time_step
    theta1 += omega1 * time_step
    theta2 += omega2 * time_step
    
    return theta1, theta2, omega1, omega2

# Animation setup
fig, ax = plt.subplots()
ax.set_aspect('equal')
ax.set_xlim(-2, 2)
ax.set_ylim(-2, 2)

line1, = ax.plot([], [], 'o-', lw=2, color='blue', label="Ball 1")
line2, = ax.plot([], [], 'o-', lw=2, color='red', label="Ball 2")
pivot, = ax.plot([], [], 'o', color='black', markersize=5)

# Initialization function
def init():
    line1.set_data([], [])
    line2.set_data([], [])
    pivot.set_data([], [])
    return line1, line2, pivot

# Update function for the animation
def animate(i):
    global theta1, theta2, omega1, omega2
    
    # Time update
    t = i * time_step
    
    # Update positions and velocities
    theta1, theta2, omega1, omega2 = update_positions(t, theta1, theta2, omega1, omega2)
    
    # Calculate the pivot position
    pivot_y = pivot_position(t)
    
    # Calculate the positions of the balls
    x1, y1 = length * np.sin(theta1), -length * np.cos(theta1) + pivot_y
    x2, y2 = length * np.sin(theta2), -length * np.cos(theta2) + pivot_y
    
    # Update line positions
    line1.set_data([0, x1], [pivot_y, y1])
    line2.set_data([0, x2], [pivot_y, y2])
    pivot.set_data([0], [pivot_y])
    
    return line1, line2, pivot

# Run the animation
ani = FuncAnimation(fig, animate, frames=500, interval=20, init_func=init, blit=True)
plt.legend()
plt.show()
