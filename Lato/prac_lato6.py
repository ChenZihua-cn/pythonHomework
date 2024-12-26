import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from scipy.integrate import solve_ivp

# Constants
g = 9.81  # gravitational acceleration (m/s^2)
L = 1.0   # length of each string (m)
m = 0.1   # mass of each ball (kg)
A = 0.1   # amplitude of vertical oscillation of the pivot (m)
omega_p = 2.0  # angular frequency of the pivot's oscillation (rad/s)
r_ball = 0.05  # radius of each ball (m)
e = 1.0   # coefficient of restitution (elastic collision)

# Equations of motion
def equations(t, y):
    theta1, z1, theta2, z2 = y
    # Pivot oscillation (upward force due to vertical oscillation)
    pivot_force = A * omega_p**2 * np.cos(omega_p * t)

    # Angular acceleration of each ball
    dtheta1 = z1
    dtheta2 = z2
    dz1 = -(g/L) * np.sin(theta1) - pivot_force * np.cos(theta1) / L
    dz2 = -(g/L) * np.sin(theta2) - pivot_force * np.cos(theta2) / L
    return [dtheta1, dz1, dtheta2, dz2]

# Collision detection and response
def handle_collision(theta1, z1, theta2, z2):
    x1, y1 = L * np.sin(theta1), -L * np.cos(theta1)
    x2, y2 = L * np.sin(theta2), -L * np.cos(theta2)
    
    # Distance between the two balls
    distance = np.sqrt((x2 - x1)**2 + (y2 - y1)**2)
    
    # If distance is smaller than 2 * radius, we have a collision
    if distance < 2 * r_ball:
        # Simple elastic collision handling (1D for simplicity)
        v1 = L * z1 * np.cos(theta1)  # velocity of ball 1
        v2 = L * z2 * np.cos(theta2)  # velocity of ball 2
        
        """
        # Use the coefficient of restitution to calculate the new velocities
        v1_new = (v1 * (m - m) + 2 * m * v2) / (m + m)
        v2_new = (v2 * (m - m) + 2 * m * v1) / (m + m)
        """

        # Use the coefficient of restitution to calculate the new velocities
        v1_new = -v1
        v2_new = -v2

        # Update the angular velocities (z1, z2)
        z1_new = v1_new / (L * np.cos(theta1))
        z2_new = v2_new / (L * np.cos(theta2))
        
        return z1_new, z2_new
    return z1, z2

# Initial conditions
theta1_initial = 0.1  # initial angle of ball 1 (radians)
theta2_initial = -0.1 # initial angle of ball 2 (radians)
z1_initial = 0.0      # initial angular velocity of ball 1 (rad/s)
z2_initial = 0.0      # initial angular velocity of ball 2 (rad/s)
y0 = [theta1_initial, z1_initial, theta2_initial, z2_initial]

# Time span
t_span = (0, 10)
t_eval = np.linspace(t_span[0], t_span[1], 1000)

# Solve the equations of motion
sol = solve_ivp(equations, t_span, y0, t_eval=t_eval, method='RK45')

# Extract results
theta1 = sol.y[0]
theta2 = sol.y[2]
z1 = sol.y[1]
z2 = sol.y[3]

# Apply collision handling after solving
for i in range(1, len(t_eval)):
    z1[i], z2[i] = handle_collision(theta1[i], z1[i], theta2[i], z2[i])

# Convert to Cartesian coordinates for animation
x1 = L * np.sin(theta1)
y1 = -L * np.cos(theta1)
x2 = L * np.sin(theta2)
y2 = -L * np.cos(theta2)

# Animation
fig, ax = plt.subplots()
ax.set_xlim(-2*L, 2*L)
ax.set_ylim(-2*L, 2*L)
ax.set_aspect('equal')
line1, = ax.plot([], [], 'ro-', lw=2, label="Ball 1")
line2, = ax.plot([], [], 'bo-', lw=2, label="Ball 2")
ax.legend()

# Initialization function for animation
def init():
    line1.set_data([], [])
    line2.set_data([], [])
    return line1, line2

# Update function for animation
def update(frame):
    thisx1 = [0, x1[frame]]
    thisy1 = [A * np.cos(omega_p * t_eval[frame]), y1[frame] + A * np.cos(omega_p * t_eval[frame])]
    
    thisx2 = [0, x2[frame]]
    thisy2 = [A * np.cos(omega_p * t_eval[frame]), y2[frame] + A * np.cos(omega_p * t_eval[frame])]
    
    line1.set_data(thisx1, thisy1)
    line2.set_data(thisx2, thisy2)
    return line1, line2

# Create and display the animation
ani = FuncAnimation(fig, update, frames=len(t_eval), init_func=init, blit=True, interval=20)
ani.save("lato-lato_solid_simulation.gif", writer="Pillow")
plt.show()





"""
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from scipy.integrate import solve_ivp

# Constants
g = 9.81  # gravitational acceleration (m/s^2)
L = 1.0   # length of each string (m)
m = 1.0   # mass of each ball (kg)
A = 0.1   # amplitude of vertical oscillation of the pivot (m)
omega_p = 2.0  # angular frequency of the pivot's oscillation (rad/s)
r_ball = 0.05  # radius of each ball (m)
e = 1.0   # coefficient of restitution (elastic collision)

# Equations of motion
def equations(t, y):
    theta1, z1, theta2, z2 = y
    # Pivot oscillation (upward force due to vertical oscillation)
    pivot_force = A * omega_p**2 * np.cos(omega_p * t)

    # Angular acceleration of each ball
    dtheta1 = z1
    dtheta2 = z2
    dz1 = -(g/L) * np.sin(theta1) - pivot_force * np.cos(theta1) / L
    dz2 = -(g/L) * np.sin(theta2) - pivot_force * np.cos(theta2) / L
    return [dtheta1, dz1, dtheta2, dz2]

# 2D Collision Detection and Response
def handle_collision_2D(x1, y1, vx1, vy1, x2, y2, vx2, vy2):
    # Relative positions and velocities
    rel_pos = np.array([x2 - x1, y2 - y1])
    rel_vel = np.array([vx2 - vx1, vy2 - vy1])
    
    # Distance between the balls
    distance = np.linalg.norm(rel_pos)
    if distance < 2 * r_ball:  # Collision detected
        # Normal vector
        normal = rel_pos / distance
        # Relative velocity along the normal
        vel_normal = np.dot(rel_vel, normal)
        # Impulse calculation
        impulse = - (1 + e) * vel_normal / (2 / m)
        impulse_vector = impulse * normal
        # Update velocities
        vx1_new = vx1 + impulse_vector[0] / m
        vy1_new = vy1 + impulse_vector[1] / m
        vx2_new = vx2 - impulse_vector[0] / m
        vy2_new = vy2 - impulse_vector[1] / m
        return vx1_new, vy1_new, vx2_new, vy2_new
    return vx1, vy1, vx2, vy2

# Initial conditions
theta1_initial = 0.1  # initial angle of ball 1 (radians)
theta2_initial = -0.1 # initial angle of ball 2 (radians)
z1_initial = 0.0      # initial angular velocity of ball 1 (rad/s)
z2_initial = 0.0      # initial angular velocity of ball 2 (rad/s)
y0 = [theta1_initial, z1_initial, theta2_initial, z2_initial]

# Time span
t_span = (0, 10)
t_eval = np.linspace(t_span[0], t_span[1], 1000)

# Solve the equations of motion
sol = solve_ivp(equations, t_span, y0, t_eval=t_eval, method='RK45')

# Extract results
theta1 = sol.y[0]
theta2 = sol.y[2]
z1 = sol.y[1]
z2 = sol.y[3]

# Convert to Cartesian coordinates
x1 = L * np.sin(theta1)
y1 = -L * np.cos(theta1)
x2 = L * np.sin(theta2)
y2 = -L * np.cos(theta2)

# Angular velocities to Cartesian velocities
vx1 = L * z1 * np.cos(theta1)
vy1 = L * z1 * np.sin(theta1)
vx2 = L * z2 * np.cos(theta2)
vy2 = L * z2 * np.sin(theta2)

# Apply collision handling at each time step
for i in range(1, len(t_eval)):
    vx1[i], vy1[i], vx2[i], vy2[i] = handle_collision_2D(
        x1[i-1], y1[i-1], vx1[i-1], vy1[i-1], x2[i-1], y2[i-1], vx2[i-1], vy2[i-1]
    )
    # Update Cartesian positions based on updated velocities
    x1[i] = x1[i-1] + vx1[i] * (t_eval[i] - t_eval[i-1])
    y1[i] = y1[i-1] + vy1[i] * (t_eval[i] - t_eval[i-1])
    x2[i] = x2[i-1] + vx2[i] * (t_eval[i] - t_eval[i-1])
    y2[i] = y2[i-1] + vy2[i] * (t_eval[i] - t_eval[i-1])

# Animation
fig, ax = plt.subplots()
ax.set_xlim(-2*L, 2*L)
ax.set_ylim(-2*L, 2*L)
ax.set_aspect('equal')
line1, = ax.plot([], [], 'ro-', lw=2, label="Ball 1")
line2, = ax.plot([], [], 'bo-', lw=2, label="Ball 2")
ax.legend()

# Initialization function for animation
def init():
    line1.set_data([], [])
    line2.set_data([], [])
    return line1, line2

# Update function for animation
def update(frame):
    thisx1 = [0, x1[frame]]
    thisy1 = [A * np.cos(omega_p * t_eval[frame]), y1[frame] + A * np.cos(omega_p * t_eval[frame])]
    
    thisx2 = [0, x2[frame]]
    thisy2 = [A * np.cos(omega_p * t_eval[frame]), y2[frame] + A * np.cos(omega_p * t_eval[frame])]
    
    line1.set_data(thisx1, thisy1)
    line2.set_data(thisx2, thisy2)
    return line1, line2

# Create and display the animation
ani = FuncAnimation(fig, update, frames=len(t_eval), init_func=init, blit=True, interval=20)
plt.show()
"""
