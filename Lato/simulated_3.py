"""

IndexError: list index out of range

"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Parameters for the simulation
r1 = 0.05  # radius of ball 1
r2 = 0.05  # radius of ball 2
pivot_x = 0  # x-position of the pivot
L1 = 1.0  # length of the first string
L2 = 1.0  # length of the second string
g = 9.81  # acceleration due to gravity

# Initial conditions for the balls
theta1 = np.pi / 4  # initial angle of ball 1 (45 degrees)
theta2 = np.pi / 4  # initial angle of ball 2 (45 degrees)
omega1 = 0.0  # initial angular velocity of ball 1
omega2 = 0.0  # initial angular velocity of ball 2

# Time step for the simulation
dt = 0.05  # time step
num_frames = 500  # number of frames to simulate

# Initial positions and velocities of the balls
x1 = np.zeros(num_frames)
y1 = np.zeros(num_frames)
x2 = np.zeros(num_frames)
y2 = np.zeros(num_frames)
vx1 = 0.1  # initial velocity of ball 1
vy1 = 0.0  # initial velocity of ball 1
vx2 = -0.1  # initial velocity of ball 2
vy2 = 0.0  # initial velocity of ball 2

# Angular velocities for the pendulums
omega1 = 0.0
omega2 = 0.0

# Initialize the figure and axes for the animation
fig, ax = plt.subplots()
ax.set_xlim(-2, 2)
ax.set_ylim(-2, 2)
ax.set_aspect('equal', adjustable='box')

# Create the pivot and balls (initially set at the pivot position)
pivot, = ax.plot([], [], 'bo', markersize=10)
ball1, = ax.plot([], [], 'ro', markersize=10)
ball2, = ax.plot([], [], 'go', markersize=10)
line1, = ax.plot([], [], 'r-', lw=2)  # Line from pivot to ball 1
line2, = ax.plot([], [], 'g-', lw=2)  # Line from pivot to ball 2

# Function to calculate the positions of the balls and update the simulation
def update(frame):
    global x1, y1, x2, y2, vx1, vy1, vx2, vy2, theta1, theta2, omega1, omega2

    # Update the angles based on angular velocities (simple pendulum dynamics)
    theta1 += omega1 * dt
    theta2 += omega2 * dt

    # Update the velocities based on simple gravity-driven equations of motion
    # Gravity forces (simplified for two coupled pendulums)
    alpha1 = (-g * (2 * r1) * np.sin(theta1)) / (L1)  # Angular acceleration for ball 1
    alpha2 = (-g * (2 * r2) * np.sin(theta2)) / (L2)  # Angular acceleration for ball 2
    omega1 += alpha1 * dt
    omega2 += alpha2 * dt

    # Update the positions based on the new angles
    x1[frame] = L1 * np.sin(theta1)
    y1[frame] = -L1 * np.cos(theta1)
    x2[frame] = L2 * np.sin(theta2)
    y2[frame] = -L2 * np.cos(theta2)

    # Check for collision between the two balls (using Euclidean distance)
    distance = np.sqrt((x1[frame] - x2[frame])**2 + (y1[frame] - y2[frame])**2)
    if distance < (r1 + r2):  # Collision threshold
        # Simple elastic collision: reverse velocities
        vx1, vy1 = -vx1, -vy1
        vx2, vy2 = -vx2, -vy2

    # Update the pivot position (it remains fixed)
    pivot.set_data([pivot_x], [0])

    # Update the ball positions in the plot
    ball1.set_data([x1[frame]], [y1[frame]])
    ball2.set_data([x2[frame]], [y2[frame]])

    # Update the lines connecting the pivot and balls
    line1.set_data([pivot_x, x1[frame]], [0, y1[frame]])
    line2.set_data([pivot_x, x2[frame]], [0, y2[frame]])

    return pivot, line1, ball1, line2, ball2

# Create the animation
ani = animation.FuncAnimation(fig, update, frames=num_frames, interval=dt*1000, blit=True)

# Save the animation as a gif
ani.save("lato_lato_simulation.gif", writer="pillow", fps=30)

# Show the animation
plt.show()
