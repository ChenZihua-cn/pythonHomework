"""
ModuleNotFoundError: No module named 'IPython'
"""

# Re-importing necessary libraries for animation in case of any reset
from IPython.display import HTML
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Function to create the dynamic plot (pendulum motion)
def animate(i):
    # Clear the previous frame
    ax.clear()
    
    # Get the current angle (theta) from the solution
    theta_current = theta[i]
    
    # Calculate the position of the ball (x, y) in Cartesian coordinates
    x = L * np.sin(theta_current)
    y = -L * np.cos(theta_current)
    
    # Set plot limits and labels
    ax.set_xlim(-L - 0.1, L + 0.1)
    ax.set_ylim(-L - 0.1, 0.1)
    ax.set_xlabel("X Position (m)")
    ax.set_ylabel("Y Position (m)")
    ax.set_title(f"Pendulum Motion at t = {t[i]:.2f} seconds")
    
    # Plot the pendulum arm and the ball
    ax.plot([0, x], [0, y], color='blue', lw=2)  # Pendulum string
    ax.plot(x, y, 'ro', markersize=10)  # Ball

    return ax,

# Create the figure and axis for the animation
fig, ax = plt.subplots(figsize=(6, 6))

# Create the animation
ani = animation.FuncAnimation(fig, animate, frames=len(t), interval=30, blit=False)

# Display the animation as HTML
HTML(ani.to_jshtml())
