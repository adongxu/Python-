import numpy as np
import matplotlib.cm as cm
import matplotlib.pyplot as plt

figsize = 7


def colormap(r): return cm.Set2(r / 20.)


N = 18  # num of bars

fig = plt.figure(figsize=(figsize, figsize))
ax = fig.add_axes([0.2, 0.2, 0.7, 0.7], polar=True)

theta = np.arange(0.0, 2 * np.pi, 2 * np.pi / N)
radii = 20 * np.random.randn(N)
width = np.pi / 4 * np.random.randn(N)
bars = ax.bar(theta, radii, width=width, bottom=0.0)
for r, bar in zip(radii, bars):
    bar.set_facecolor(colormap(r))
    bar.set_alpha(0.6)

plt.show()