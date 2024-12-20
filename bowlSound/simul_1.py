"""
用颜色模拟水的振幅，但是模拟的质量有待提高

"""


import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from scipy.integrate import solve_ivp

# Parameters
bowl_radius = 1.0      # Radius of the bowl
grid_points = 1000     # Number of points for simulation grid
time_steps = 20       # Frames for animation
dt = 0.005              # Time step for animation

# Generate grid
x = np.linspace(-bowl_radius, bowl_radius, grid_points)
y = np.linspace(-bowl_radius, bowl_radius, grid_points)
X, Y = np.meshgrid(x, y)
R = np.sqrt(X**2 + Y**2)

# Function for bowl vibration
def bowl_vibration(t):
    """
    Simulates multi-frequency bowl vibration with spatial decay.
    """
    return (np.sin(2 * np.pi * 3 * t) + 0.5 * np.sin(2 * np.pi * 5 * t)) * np.exp(-R**2)

# Water wave equation with damping and nonlinearity
def wave_equation(t, Z):
    """
    Solves water wave dynamics with damping and nonlinearity.
    Z: Flattened state vector containing displacement and velocity.
    """
    damping = 0.1       # Damping coefficient
    nonlinearity = 0.2  # Nonlinearity coefficient
    
    # Reshape Z into two components: displacement and velocity
    Z_reshaped = Z.reshape((2, grid_points, grid_points))
    displacement, velocity = Z_reshaped
    
    # Compute acceleration (wave dynamics)
    acceleration = -4 * np.pi**2 * displacement - damping * velocity - nonlinearity * displacement**3
    return np.vstack([velocity, acceleration]).flatten()

# Initial conditions: still water (zero displacement and velocity)
Z0 = np.zeros((2, grid_points, grid_points)).flatten()

# Solve the wave equation over time
time_eval = np.linspace(0, time_steps * dt, time_steps)
sol = solve_ivp(wave_equation, [0, time_steps * dt], Z0, t_eval=time_eval)

# Extract displacement over time
displacements = sol.y[:grid_points**2 * time_steps].reshape((time_steps, 2, grid_points, grid_points))
displacement = displacements[:, 0]  # Extract displacement component only

# Animation setup
fig, ax = plt.subplots(figsize=(6, 6))
ax.set_xlim(-bowl_radius, bowl_radius)
ax.set_ylim(-bowl_radius, bowl_radius)
ax.axis('off')

# Initial visualization
surf = ax.imshow(bowl_vibration(0), extent=(-bowl_radius, bowl_radius, -bowl_radius, bowl_radius),
                 cmap='viridis', vmin=-1, vmax=1, interpolation='bicubic')

# Update function for animation
def update(frame):
    """
    Updates the animation frame by combining bowl vibration and water surface dynamics.
    """
    combined_vibration = bowl_vibration(frame * dt) + displacement[frame]
    surf.set_array(combined_vibration)
    return surf,

# Create and save the animation
ani = FuncAnimation(fig, update, frames=time_steps, blit=True)
ani.save("bowl_water_simulation.gif", writer="pillow")
plt.show()
