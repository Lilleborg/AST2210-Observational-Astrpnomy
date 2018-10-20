import numpy as np
from math import sqrt

topp = 18.1
top_unc = 0.1
max_c = 255.
RGBmax = np.asarray([8.9,12.2,1.9])
RGBunc = np.asarray([0.3,0.2,0.4])

RGB_c = RGBmax*max_c/topp
RGB_unc = sqrt(np.sum((RGBunc/RGBmax)**2))*RGB_c

print 'Max pixel value RGB colors'
print 'Red: {:.0f} pm {:.0f}'.format(round(RGB_c[0]),round(RGB_unc[0]))
print 'Green: {:.0f} pm {:.0f}'.format(round(RGB_c[1]),round(RGB_unc[1]))
print 'Blue: {:.0f} pm {:.0f}'.format(round(RGB_c[2]),round(RGB_unc[2]))