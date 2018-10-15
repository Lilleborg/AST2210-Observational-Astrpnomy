import numpy as np
import imageio	# may be installed with: pip install imageio
import matplotlib.pyplot as plt
from matplotlib import rcParams
from math import sqrt
from histogram_BIAS_max_dark import reading
from mean_noise import noisetwo

def noise_dynamic_normed(images):
	"""
	Returns normalized noise of dynamic number of images
	@ images[N,[x,y]] - list with 2D arrays as elements
		@ N - number of images in images, min value 2
		@ x - number of pixels in x-direction
		@ y - number of pixels in y-direction
	"""
	N = np.size(images,axis=0)
	if N == 2:	# if only two images
		return noisetwo(images[0],images[1])
	else:
		n = N/2.	# number of pairs
		even = np.zeros_like(images[0])
		odd = np.zeros_like(images[0])
		for i in np.arange(0,N-1,2):
			even += images[i]	#summing images with even index
			odd += images[i+1]	#summing images with odd index
		return noisetwo(odd,even)/n	# returning normalized noise

if __name__ == '__main__':
	# Path extension
	path = '../images/ex3_4_5/flatfield_'

	# Reading
	N_images = 16
	
	many_im = []
	for k in range(1,N_images+1):
		ending = str(k)+'.bmp'
		many_im.append(reading(path+ending))
	
	# Calculating and filling arrays
	n = np.arange(1,N_images/2+1)	# pairs array
	noise_pairs = []				# list with noise from pairs
	for i in range(N_images/2):
		noise_pairs.append(noise_dynamic_normed(many_im[:2*i+2]))
	exact_one_pair = noise_dynamic_normed(many_im[:2])
	
	# Plotting
	font = {'size'   : 12}
	plt.matplotlib.rc('font', **font)
	rcParams.update({'figure.autolayout': True})

	plt.title('Noise in composite flat field images')
	plt.plot(n,exact_one_pair/np.sqrt(n),'-.',label='exact')
	plt.plot(n,noise_pairs,label='normalized sum')
	plt.ylabel('Standard deviation of pixel values')
	plt.xlabel('Number of pairs in composite image')
	plt.tight_layout()
	plt.legend()
	plt.savefig('noise_composite.pdf')
	plt.show()