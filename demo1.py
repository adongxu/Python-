from matplotlib.pyplot import *

# some simple data
x = [1,2,3,4]
y = [5,4,3,2]

# create new figure
figure('sample charts')

# divide subplots into 2x3 grid and select #1
subplot(231)
plot(x,y)

# select #2
subplot(232)
bar(x,y)

# horizontal bar
subplot(233)
barh(x,y)

# create stacked bar charts
subplot(234)
bar(x,y)

y1 = [7,8,5,3]
bar(x,y, bottom=y,color='r')

# box plot
subplot(235)
boxplot(x)

# scatter plot
subplot(236)
scatter(x,y)

show()