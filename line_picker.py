import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 10, 100)

fig, ax = plt.subplots()
plt.axvline(x=1500, picker=5)
# for i in range(1, 10):
#     ax.plot(x, i * x + x, picker=5)

def on_pick(event):
    event.artist.set_visible(not event.artist.get_visible())
    fig.canvas.draw()

fig.canvas.callbacks.connect('pick_event', on_pick)
plt.show()