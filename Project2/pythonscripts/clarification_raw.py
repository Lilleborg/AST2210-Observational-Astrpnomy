import numpy as np
import imageio	# may be installed with: pip install imageio
import matplotlib.pyplot as plt
from matplotlib import rcParams
#from math import sqrt
from histogram_BIAS_max_dark import reading,print_info
import sys

if __name__ == '__main__':
	# Path extension
	path = '../images/ex3_4_5/'

	#$ Reading
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

	## Calculating
	avr_flats = np.sum(many_flats,axis=0)/N_flats
	avr_dark_flats = np.sum(many_dark_flats,axis=0)/N_darks
	avr_dark_raw = np.sum(many_dark_raw,axis=0)/N_darks

	master_flat = avr_flats - avr_dark_flats 
	normed_master_flat = master_flat/master_flat.mean()

	corrected_I = ((raw_I-avr_dark_raw)/np.round(normed_master_flat)).astype(np.uint8)
	print_info(corrected_I,'corrected_I')

	filename = 'corrected_I'
	if hole:
		filename += '_hole'
	filename += '.bmp'
	imageio.imwrite(filename,corrected_I)
	if hole != True:
		sys.exit()

	shine_crit = 82
	mini_crit = 4
	
	sumrows = np.sum(corrected_I,axis=1)/752	# mean row values
	
	shiningrows = corrected_I[sumrows>shine_crit]	# rows with high brightness
	focus = shiningrows[1]							# focus row for minimas
	minimas = np.asarray(np.nonzero(focus<=mini_crit))[0]	# minimas indices
	truemini = [minimas[4]]	# picked start, 
	for i in range(1,len(minimas)):
		if abs(minimas[i]-truemini[-1]>=10):
			truemini.append(minimas[i])

	sumrows_raw = (np.sum(raw_I,axis=1)/752).astype(int)	# mean row values
	shinging_raw = corrected_I[sumrows_raw>=sumrows_raw.max()]	# rows with high brightness
	mean_raw = corrected_I[sumrows_raw==int(sumrows_raw.mean())]# rows with mean brightness

	print_info(raw_I,'Raw image')
	print_info(shinging_raw[0],'bright row')
	print_info(mean_raw[10],'mean row')


	## Plotting
	font = {'size'   : 12}
	plt.matplotlib.rc('font', **font)
	rcParams.update({'figure.autolayout': True})

	plt.figure(1)
	plt.subplot(211)
	plt.title('Pixel values in two rows of raw image')
	plt.plot(shinging_raw[0],label='Pixel row %d'%(np.nonzero(sumrows_raw>=sumrows_raw.max())[0][0]))
	plt.ylabel('Pixel value')
	plt.xlabel('Pixel number')
	plt.tight_layout()
	plt.legend()
	plt.subplot(212)
	plt.plot(mean_raw[10],label='Pixel row %d'%(np.nonzero(sumrows_raw==int(sumrows_raw.mean()))[0][10]))
	plt.ylabel('Pixel value')
	plt.xlabel('Pixel number')
	plt.tight_layout()
	plt.legend()
	plt.savefig('pixelrows.pdf')

	plt.figure(2)
	plt.title('Amount of pixels between minima of order 4')
	plt.plot(focus,label="Signal")
	plt.plot([truemini[0],truemini[-2]],[focus[truemini[0]],focus[truemini[-2]]],'-o')
	plt.text(0,150,"Line between\n4th minima\nLength = %d"%(truemini[-2]-truemini[0]))
	plt.arrow(0,145,300,-140, width = 1)
	plt.ylabel('Pixel value')
	plt.xlabel('Pixel number')
	plt.tight_layout()
	plt.legend()
	plt.savefig('pixellength.pdf')

	plt.show()