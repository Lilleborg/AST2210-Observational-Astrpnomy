import numpy as np
import matplotlib.pyplot as plt
from math import ceil
from matplotlib import rcParams

# Vectors
n = int(2**15)		# int. points
x = np.linspace(0,1,n)	# mesh points
signal_up = np.zeros(n)	# signal array
signal_down = np.ones_like(signal_up)	# array like signal

# Set signal and FFT
signal_up[int(n/2-50):int(ceil(n/2+50))] = 1	# initializing elements
signal_down[int(n/2-5000):int(ceil(n/2+5000))] = 0.2	# int(n/4):int(ceil(3*n/4.))
fft_up = np.fft.fft(signal_up)			# fft of signals
fft_up = fft_up/np.max(fft_up)
fft_down = np.fft.fft(signal_down)
fft_down = fft_down/np.max(fft_down)

plotting = np.asarray([[signal_up,np.abs(fft_up)],[signal_down,np.abs(fft_down)]])	# storing results
freq = np.fft.fftfreq(n)
labels = ["Shape of single slit","Shape of anti-slit"]

# Plotting
font = {'size'   : 12}
plt.matplotlib.rc('font', **font)
rcParams.update({'figure.autolayout': True})
for i in range(2):
	plt.figure(i)
	plt.subplot(211)
	plt.title("Aperture shape")
	plt.plot(x,plotting[i,0],label=labels[i])
	plt.legend()
	plt.ylabel("Intensity exiting slit")
	plt.subplot(212)
	plt.title("Fourier transform of aperture shape")
	plt.plot(freq[n/2:],plotting[i,1][n/2:],"r",freq[0:n/2-1],plotting[i,1][0:n/2-1],"r")
	plt.ylabel("Intensity diffraction pattern")
	plt.xlabel("Distance from center minima")
	plt.savefig("FFT_single_slit"+str(i)+".pdf")
"""
plt.figure(2)
plt.plot(freq[n/2:],plotting[0,1][n/2:],"r",freq[0:n/2-1],plotting[0,1][0:n/2-1],"r")
plt.ylabel("Intensity diffraction pattern")
plt.xlabel("Distance from center minima")
plt.savefig("FFT_only.pdf")

plt.figure(3)
plt.plot(freq[n/2:],plotting[0,1][n/2:],"r")
plt.ylabel("Intensity diffraction pattern")
plt.xlabel("Distance from center minima")
plt.savefig("FFT_left_only.pdf")
"""
plt.show()