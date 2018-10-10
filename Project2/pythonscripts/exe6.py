import numpy as np
import imageio
import sys
import matplotlib.pyplot as plt

ex2_paths = '../images/ex2/'
ex3_4_5_paths = '../images/ex3_4_5/'

im_bias = np.asarray(imageio.imread(ex3_4_5_paths+'bias_min_expo1.bmp'))
im_dark_max = np.asarray(imageio.imread(ex3_4_5_paths+'dark_max_expo.bmp'))

bias_info = [np.mean(im_bias),im_bias.min(),im_bias.max()]
dark_info = [np.mean(im_dark_max),im_dark_max.min(),im_dark_max.max()]

print ('Mean,minimum and maxima from first BIAS: {:.3f}, {:d}, {:d}'.format(*bias_info))
print ('Mean,minimum and maxima from max exposure dark {:.3f}, {:d}, {:d}'.format(*dark_info))
#plt.hist(im_bias,bins = 50)
#plt.show()
hist_bias,bins_bias = np.histogram(im_bias,bins = 'auto')
hist_dark,bins_dark = np.histogram(im_dark_max,bins = 'auto')


plt.figure(1)
plt.bar(bins_bias[:-1],hist_bias,width=0.1)

plt.figure(2)
plt.bar(bins_dark[:-1],hist_dark,width=0.5)
plt.show()