import numpy as np
import matplotlib.pyplot as plt
from matplotlib import animation

fig = plt.figure()
ax = plt.axes(xlim=(0,2),ylim=(-2,2))
line, = ax.plot([],[],lw=2)

def init():
    # create current frame
    line.set_data([], [])
    return line,

def animate(i):
    # draw picture
    x = np.linspace(0,2,1000)
    y = np.sin(2*np.pi*(x-0.01*i))*np.cos(22*np.pi*(x-0.01*i))
    line.set_data(x,y)
    return line,

animator = animation.FuncAnimation(fig, animate, init_func=init,frames=200,
                                   interval=20, blit=True)

plt.show()