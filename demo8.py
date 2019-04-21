import numpy as np
import matplotlib.pyplot as plt

# generate number of measurements
x = np.arange(1,10,1)

# values computed from "measured"
y = np.log(x)

# add some error samples from standard normal distribution
xe = 0.1*np.abs(np.random.randn(len(y)))
print(xe)
# draw and show error bar
plt.bar(x,y,yerr=xe,width=0.4,align='center', ecolor='r',color='cyan',
        label='experiment #1')

# give some explainations
plt.xlabel('# measurement')
plt.ylabel('Measured values')
plt.title('Measurements')
plt.legend(loc='upper left')

plt.show()