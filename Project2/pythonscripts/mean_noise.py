import numpy as np
from math import sqrt
import imageio	# may be installed with: pip install imageio
from histogram_BIAS_max_dark import reading,print_info

def meantwo(im1,im2):
	"""
	Returns mean value of the sum of two images
	@ im1 - 2D array image1
	@ im2 - 2D array image2
	"""
	added = im1+im2
	return added.mean()

def noisetwo(im1,im2):
	"""
	Returns noise from two images by standard deviation of the differance
	@ im1 - 2D array image1
	@ im2 - 2D array image2
	"""
	subbed = im1-im2
	return subbed.std()

if __name__ == '__main__':
	# Path extension
	path = '../images/ex3_4_5/'
		
	# Read images
	im_bias1 = reading(path+'bias_min_expo1.bmp')
	im_bias2 = reading(path+'bias_min_expo2.bmp')
	im_flat1 = reading(path+'flatfield_1.bmp')
	im_flat2 = reading(path+'flatfield_2.bmp')

	# Computing
	mean_bias = meantwo(im_bias1,im_bias2)
	noise_bias = noisetwo(im_bias1,im_bias2)
	mean_dark = meantwo(im_flat2,im_flat1)
	noise_dark = noisetwo(im_flat1,im_flat2)
	g = (mean_dark-mean_bias)/(noise_dark**2-noise_bias**2)
	noise_one_bias = noise_bias/sqrt(2.)
	RON = g*noise_one_bias

	# Printing
	print_info(im_bias1+im_bias2,'Composite bias')
	print 'Noise of two bias frames: {:.5f}\n'.format(noise_bias)
	print 'Noise of a single bias frame: {:.5f}\n'.format(noise_one_bias)
	print_info(im_flat1+im_flat2,'Composite flat')
	print 'Noise of two flat frames: {:.5f}\n'.format(noise_dark)
	print 'Conversion factor:'
	print 'Value in electrons/ADU: {:.5f}\n'.format(g)
	print 'Readout noise:'
	print 'Noise from one bias frame in electrons: {:.5f}'.format(RON)

