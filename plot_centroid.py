import h5py
import matplotlib.pyplot as plt
from scipy.stats import norm
import numpy as np

filename = "centroid.hdf5"

with h5py.File(filename, "r") as f:
    print("Keys: %s" % f.keys())
    a_group_key = list(f.keys())[0]
    data = list(f[a_group_key])

x = []
y = []
x_size = data[0][2]
y_size = data[0][3]
print('-' * 20)
print(x_size)
print('-'*20)
for i in range(0, len(data)):
    x.append(data[i][0])
    y.append(x_size - data[i][1])

meanx, stdx = norm.fit(x)
meany, stdy = norm.fit(y)

plt.subplot(222)
plt.hist(x, density=True)
xmin, xmax = plt.xlim()
x_vec = np.linspace(xmin, xmax, 100)
gauss_x_y = norm.pdf(x_vec, meanx, stdx)
plt.subplot(223)
plt.hist(y, density=True)
ymin, ymax = plt.xlim()
y_vec = np.linspace(ymin, ymax, 100)
gauss_y_y = norm.pdf(y_vec, meany, stdy)
plt.plot(y_vec, gauss_y_y)
plt.subplot(224)
plt.plot(x, y, 'ro')
plt.axis([0,y_size, 0, x_size])
plt.show()
