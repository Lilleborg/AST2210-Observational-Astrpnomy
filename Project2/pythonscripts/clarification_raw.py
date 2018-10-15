import numpy as np
import imageio	# may be installed with: pip install imageio
#import matplotlib.pyplot as plt
#from matplotlib import rcParams
#from math import sqrt
from histogram_BIAS_max_dark import reading,print_info

if __name__ == '__main__':
	# Path extension
	path = '../images/ex3_4_5/'

	# Reading
	N_flats = 16
	N_darks = 5
	hole = True

	raw_I = reading(path+'diffraction1_excercise4.bmp',hole)
	
	many_flats = []
	many_dark_flats = []
	many_dark_raw = []

	for k in range(1,N_flats+1):
		ending = 'flatfield_'+str(k)+'.bmp'
		many_flats.append(reading(path+ending,hole))
	for k in range(1,N_darks+1):
		ending = str(k)+'.bmp'
		many_dark_flats.append(reading(path+'dark_flat'+ending,hole))
		many_dark_raw.append(reading(path+'dark_same_expo_'+ending,hole))
	many_flats = np.asarray(many_flats)
	many_dark_flats = np.asarray(many_dark_flats)
	many_dark_raw = np.asarray(many_dark_raw)

	avr_flats = np.sum(many_flats,axis=0)/N_flats
	avr_dark_flats = np.sum(many_dark_flats,axis=0)/N_darks
	avr_dark_raw = np.sum(many_dark_raw,axis=0)/N_darks

	master_flat = avr_flats - avr_dark_flats 
	normed_master_flat = master_flat/master_flat.mean()

	corrected_I = ((raw_I-avr_dark_raw)/np.round(normed_master_flat)).astype(np.uint8)
	print_info(corrected_I,'corrected_I')
	print corrected_I.shape
	filename = 'corrected_I'
	if hole:
		filename += '_hole'
	filename += '.bmp'
	imageio.imwrite(filename,corrected_I)