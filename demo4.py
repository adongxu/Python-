from pylab import *
import matplotlib as mpl
import datetime

fig = figure()

# get current axis
ax = gca()

# set some date range
start = datetime.datetime(2013,1,1)
stop = datetime.datetime(2013,12,31)
delta = datetime.timedelta(days=1)

# convert date for matplotlib
dates = mpl.dates.drange(start, stop, delta)

# generate some random values
values = np.random.rand(len(dates))

# create plot with dates
ax.plot_date(dates, values, linestyle='-', marker='')

# specify format
date_format =mpl.dates.DateFormatter('%Y-%m-%d')

# apply format
ax.xaxis.set_major_formatter(date_format)

# auto format date labels
# rotates labels by 30 degrees by default
# use rotate param to specify different rotation degree
# user bottom param to give more room to date labels
fig.autofmt_xdate()

show()