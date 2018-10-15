import numpy as np
import imageio	# may be installed with: pip install imageio
import matplotlib.pyplot as plt
from matplotlib import rcParams

def reading(path,hole = False, sides = 300):
	"""
	Reads image file and return as 2D array
	@ path - path to filename
	@ hole - return array of the hole image if True, default to False
	@ sides - gives length of sides of central region if hole = False
	"""
	im1 = np.asarray(imageio.imread(path)).astype(int)
	if hole:
		return im1
	else:	# return using indices from top left corner of central region 
		tl = (np.asarray(im1.shape)/2.0-1-sides/2).astype(int)
		return im1[tl[0]:tl[0]+sides,tl[1]:tl[1]+sides]

def info(im1):
	"""
	Returns mean, min and max of pixel values, as well as index of max value
	@ im1 - 2D array image
	"""
	return [np.mean(im1),im1.min(),im1.max(),\
			np.unravel_index(im1.argmax(),im1.shape)]

def print_info(im,name):
	print ('For '+name)
	infom = info(im)
	print ('Mean, minimum, maxima pixel values: '\
			+'{:.3f}, {:.1f}, {:.1f}'.format(*infom[:-1]))
	print ('Index of maxima: {:s}'.format(infom[-1])+'\n')

if __name__ == '__main__':
	# Path extension
	path = '../images/ex3_4_5/'

	# Read images
	im_bias = reading(path+'bias_min_expo1.bmp')
	im_dark_max = reading(path+'dark_max_expo.bmp')

	print_info(im_bias,'First bias')
	print_info(im_dark_max,'Max exposure dark')

	# Plotting
	font = {'size'   : 12}
	plt.matplotlib.rc('font', **font)
	rcParams.update({'figure.autolayout': True})

	hist_bias,bins_bias = np.histogram(im_bias,bins = 'auto')
	hist_dark,bins_dark = np.histogram(im_dark_max,bins = 'auto')

	plt.figure(1)
	plt.title('Historgram pixel value bias1 frame')
	plt.bar(bins_bias[:-1],hist_bias,width=bins_bias[-1]/100)
	plt.xlabel('Pixel value, intensity')
	plt.ylabel('Number of pixels')
	plt.savefig('hist_pixel_bias1.pdf')

	plt.figure(2)
	plt.title('Historgram pixel value max expo dark frame')
	plt.bar(bins_dark[:-1],hist_dark,width=bins_dark[-1]/100)
	plt.xlabel('Pixel value, intensity')
	plt.ylabel('Number of pixels')
	plt.savefig('hist_pixel_darkmax.pdf')
	plt.show()
