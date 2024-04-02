from matplotlib.animation import FuncAnimation
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import matplotlib.widgets as widgets
import random

# Initial width and height
width = 50
height = 50

# Initial center of gravity (COG)
cog_x = width / 2
cog_y = height / 2

# Create the plot and frame
fig, ax = plt.subplots()
rectangle = patches.Rectangle((0, 0), width, height, fill=False)
ax.add_patch(rectangle)
scat = ax.scatter(cog_x, cog_y, color='red')

# Create sliders for width and height
ax_width = plt.axes([0.25, 0.1, 0.65, 0.03])
slider_width = widgets.Slider(ax_width, 'Width', 0.1, 100, valinit=width)

ax_height = plt.axes([0.25, 0.15, 0.65, 0.03])
slider_height = widgets.Slider(ax_height, 'Height', 0.1, 100, valinit=height)

# Function to update the data and graph
def update(frame):
    # Update width and height from sliders
    width = slider_width.val
    height = slider_height.val

    # Update COG
    global cog_x, cog_y
    cog_x += 1  # Increase COG x-coordinate by 1 each second
    cog_y += 1  # Increase COG y-coordinate by 1 each second

    # Update rectangle and scatter plot
    rectangle.set_width(width)
    rectangle.set_height(height)
    scat.set_offsets((cog_x, cog_y))

# Animation function
anim = FuncAnimation(fig, update, frames=None, interval=1000)  # Interval is in milliseconds (1000ms = 1 second)
plt.show()