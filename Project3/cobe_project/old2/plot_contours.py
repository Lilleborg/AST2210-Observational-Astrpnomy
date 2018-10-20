# Simple contour plotting script for visualizing the lnL computed by
# cmb_likelihood.py. 
# For convenience, it takes as input either the .npy file or the .dat file.
# In the .dat case you also have to supply the number of grid points in each 
# direction so that we can define the grid correctly.

import numpy as np
import matplotlib.pyplot as plt
import sys

if __name__ == "__main__":
    if len(sys.argv)<2:
        print 'Wrong number if input arguments.'
        print 'Usage: python plot_contours.py resultfile.npy'
        print 'Or: python plot_contours.py resultfile.dat numpoints_Q numpoints_n'
        sys.exit()

    inputfile = sys.argv[1]
    if inputfile[inputfile.rfind('.'):]=='.npy':
        a = np.load(inputfile)
        Q_values = a[0,:]
        n_values = a[1,:]
        lnL = a[2:,:]
        qgrid, ngrid = np.meshgrid(Q_values,n_values, indexing='ij')

    else: # ascii file
        n_Q = int(sys.argv[2])
        n_n = int(sys.argv[3])
        a = np.loadtxt(inputfile)
        qgrid = np.reshape(a[:,0],(n_Q, n_n))
        ngrid = np.reshape(a[:,1],(n_Q, n_n))
        lnL = np.reshape(a[:,2],(n_Q, n_n))
        Q_values = qgrid[:,0]
        n_values = ngrid[0,:]

    lnL -= np.amax(lnL) # arbitrarily "normalizing" to make the numbers more manageable

    # For a Gaussian distribution, the 1, 2 and 3 sigma (68%, 95% and
    # 99.7%) confidence regions correspond to where -2 lnL increases by
    # 2.3, 6.17 and 11.8 from its minimum value. 0.1 is close to the
    # peak. 
    my_levels = [0.1, 2.3, 6.17, 11.8]
    cs = plt.contour(qgrid,ngrid, -2.*lnL, levels=my_levels, colors='k')
    plt.grid()
    plt.show()
