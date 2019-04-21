from pylab import *
import numpy as np

# generate uniformly distributed 256 points
# form -pi to pi,inclusive
x = np.linspace(-np.pi, np.pi,256,endpoint=True)

# these are vectorised versions of math.cos, and math.sin in built-in Python
# maths compute cos for every x
y = np.cos(x)

# compute sin for every x
y1 = np.sin(x)

# plot cos
plot(x, y, linewidth=3.0)

# plot sin
plot(x,y1)

# define plot title
title('Functions $\sin$ and $\cos$')

# set x limit
xlim(-3.0,3.0)
# set y limit
ylim(-1.0,1.0)

# format ticks at specific values $-\pi$可以显示希腊字母
xticks([-np.pi, -np.pi/2,0,np.pi/2,np.pi],['$-\pi$', '$-\pi/2$',
                                           '$0$','$+\pi/2$', '$+\pi$'])
yticks([-1,0,1], ['$-1$', '$0$', '$+1$'])

show()