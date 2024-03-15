import matplotlib.pyplot

fig, ax = matplotlib.pyplot.subplots()

width = 50
height = 50

cog = (width / 2, height / 2)

rectangle = matplotlib.patches.Rectangle((0, 0), width, height, fill=False)

ax.add_patch(rectangle)

scat = ax.scatter(*cog, color='red')

ax_width = matplotlib.pyplot.axes([0.25, 0.1, 0.65, 0.03])
slider_width = matplotlib.widgets.Slider(ax_width, 'Width', 0.1, 100, valinit=width)

ax_height = matplotlib.pyplot.axes([0.25, 0.15, 0.65, 0.03])
slider_height = matplotlib.pyplot.Slider(ax_height, 'Height', 0.1, 100, valinit=height)

def update(val):
    width = slider_width.val
    height = slider_height.val

    cog = (width / 2, height / 2)

    rectangle.set_width(width)
    rectangle.set_height(height)
    scat.set_offsets(cog)

    fig.canvas.draw_idle()

slider_width.on_changed(update)
slider_height.on_changed(update)

matplotlib.pyplot.show()
