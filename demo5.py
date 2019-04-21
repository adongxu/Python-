from matplotlib.pyplot import *

# generate different normal distributions
x1 = np.random.normal(30, 3, 100)
x2 = np.random.normal(20, 2, 100)
x3 = np.random.normal(10, 3, 100)

# plot item
plot(x1, label='plot')
plot(x2, label='2nd plot')
plot(x3, label='last plot')

# generate a legend box
# start pos=(0,1.02) width=1,height=0.102
# cols=3, loc=3='lower left' mode=None/expand:水平扩展至整个坐标轴区域
# borderaxespad:坐标轴和图例边界之间的间距
legend(bbox_to_anchor=(0., 1.02, 1., .102), loc=3, ncol=3,
       mode='expand', borderaxespad=0.)

# annotate an important value
# 为(55,20)的点给了一个字符串描述 xycoords='data':注解和数据使用相同的坐标系
# xytext=(5, 38):注解文本的起始位置
# arrowprops=dict(arrowstyle='->') text->data arrowstyle指定箭头风格
annotate('Important value', (55, 20), xycoords='data', xytext=(5, 38),
         arrowprops=dict(arrowstyle='->'))

show()
