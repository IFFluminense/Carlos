
from matplotlib.animation import FuncAnimation
import matplotlib.pyplot
import random
 
# creating the first plot and frame
fig, ax = matplotlib.pyplot.subplots()

width = 50
height = 50

cog = (width/2, height/2)

rectangle = matplotlib.patches.Rectangle((0, 0), width, height, fill=False)

ax.add_patch(rectangle)

scat = ax.scatter(*cog, color='red')

ax_width = matplotlib.pyplot.axes([0.25, 0.1, 0.65, 0.03])
slider_width = matplotlib.widgets.Slider(ax_width, 'Width', 0.1, 100, valinit=width)

ax_height = matplotlib.pyplot.axes([0.25, 0.15, 0.65, 0.03])
slider_height = matplotlib.pyplot.Slider(ax_height, 'Height', 0.1, 100, valinit=height)
x = 0
y = 0
 
def update(frame):
    global x, y

    width = slider_width.val
    height = slider_height.val

    x = x + 1
    y = y + 1

    cog = (x, y)  

    print(cog)

    rectangle.set_width(width)
    rectangle.set_height(height)
    scat.set_offsets(cog)
 
anim = FuncAnimation(fig, update, frames = None, interval = 1000)
matplotlib.pyplot.show()