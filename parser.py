import glob
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


namelist = glob.glob("scanme/*.txt")

l = [pd.read_csv(filename, sep='\t', header=None, names = ["Raman shift, cm^{-1}", filename]) for filename in namelist]

# # **************** Merging DataFrames on Raman Shift ******************************
# myData = l
# for a in range(len(l)-1):
#     myData[a+1] = myData[a].merge(l[a+1], on="Raman shift, cm^{-1}", how="outer")
# print(myData[-1])
# # *********************

# ************** Make niceLook and dynamic pick *******************
colorlist = [(102/255, 94/255, 252/255),(255/255, 175/255, 43/255),(255/255, 81/255, 152/255), (0, 179/255, 0), (59/255, 217/255, 233/255), (188/255, 0, 188/255)] #blue, orange, magenta, green, cyan, purple

fig, ax = plt.subplots()

ax.set(ylabel='Intensity, a.u.')
plt.axvline(x=1580, picker=5) #G-line
plt.axvline(x=1350, picker=5) #D-line
plt.axvline(x=2700, picker=5) #2D-line
plt.axvline(x=1333, picker=5) #Dimaond-line
plt.axvline(x=972, picker=5) #Si-line (one more is 520)

def on_pick(event):
    event.artist.set_visible(not event.artist.get_visible())
    fig.canvas.draw()

fig.canvas.callbacks.connect('pick_event', on_pick)

# *************************************

# ax = l[0].plot(subplots=True, x="Raman shift, cm^{-1}", ms=10, lw=2, alpha=0.7, title="Raman spectra from parced files") # for plots in one figure
l[0].plot(ax=ax, subplots=True, x="Raman shift, cm^{-1}", ms=10, lw=2, alpha=0.7, title="Raman spectra from parced files")

for a in range(len(l)-1):
    l[a+1].plot(ax=ax, subplots=True, x="Raman shift, cm^{-1}", ms=10, lw=2, alpha=0.7, color=colorlist[a%len(colorlist)])






plt.show()

# df.plot(x='x', y=['p1','p2'], style=['-o','-.'], ms=10, lw=2, alpha=0.7)
# plt.show()

# df = pd.DataFrame({"x": np.linspace(0.0, 5.0, num=500),
#                        "p1": 101.325*1000/760/5 * np.linspace(0.0, 5.0, num=500),
#                        "p2": 101.325/5* np.linspace(0.0, 5.0, num=500)})


# -----------------------
# Plotting
#
# df.plot(x='x', y=['p1','p2'], style=['-o','-.'], ms=10, lw=2, alpha=0.7)
# # data50.plot(x='time', y='pressure50')
# plt.show()

# myData.plot(x='time', y=['pressure25','pressure50'])


