import numpy as np
import matplotlib.pyplot as plt
import matplotlib.transforms as transforms

def setup(layout=None):
    assert layout is not None

    fig = plt.figure()
    ax = fig.add_subplot(layout)
    return fig, ax

def get_signal():
    t = np.arange(0., 2.5, 0.01)
    s = np.sin(5*np.pi*t)
    return t,s

def plot_signal(t,s):
    line, = plt.axes().plot(t,s,linewidth=5, color='magenta')
    return line,

def make_shadow(fig, axes, line, t,s):
    # how many points to move the shadow
    delta = 2 / 72
    offset = transforms.ScaledTranslation(delta, -delta, fig.dpi_scale_trans)
    offset_transform = axes.transData + offset

    # we plot the same data,but now using offset transform
    # zorder -- to render it below the line
    axes.plot(t,s,linewidth=5,color='grey',transform=offset_transform, zorder=0.5*line.get_zorder())

if __name__ == '__main__':
    fig,axes = setup(111)
    t,s = get_signal()
    line, = plot_signal(t,s)

    make_shadow(fig, axes,line,t,s)

    axes.set_title('Shadow effect using an offset transform')

    plt.show()