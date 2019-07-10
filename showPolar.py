import sys
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

im = Image.open ( sys.argv [ 1 ] )

w, h = im.size
rgb = np.array ( im.getdata ( ) ).reshape ( h, w, 3 ) / 255.0
hsv = np.array ( im.getdata ( ).convert ( 'HSV' ) ).reshape ( h, w, 3 ) / 255.0
xlim = 400
if xlim > w : xlim = w
ylim = 1000
if ylim > h : ylim = h

if xlim is not None and xlim > 0 :
    w = xlim
    #rgb = rgb [ :xlim ]
    #hsv = hsv [ :xlim ]
if ylim is not None and ylim > 0 :
    h = ylim
    #rgb = rgb [ :, :ylim ]
    #hsv = hsv [ :, :ylim ]
rgb = rgb [ :h, :w ]
hsv = hsv [ :h, :w ]

fig = plt.figure()

ax=fig.add_subplot ( 121 )
ax.imshow ( rgb, )

ax=fig.add_subplot ( 222, projection='polar' )
sc=ax.scatter ( hsv[...,0] * 2.0 * np.pi, hsv[...,2],
        s=hsv[...,1]*10,
        c=rgb.reshape ( (w*h,3) ),
        alpha=0.6 )
#ax.set_thetalim ( 0,0xffffff )
#ax.set_thetalim ( 0,255 )
#ax.set_thetamin ( 0.0 )
#ax.set_thetamax ( 1.0 )
#ax.set_rlim ( 0,255 )
ax.set_rmin ( 0.0 )
ax.set_rmax ( 1.0 )
ax.set_ylim ( ymin=0, ymax=1.0 )
#ax.set_xlim ( 0,255 )
ax.set_yticks ( [] )
ax.set_xticks ( [] )

ax=fig.add_subplot ( 224, projection='polar' )
sc=ax.scatter ( hsv[...,0] * 2.0 * np.pi, hsv[...,1],
        s=hsv[...,2]*10,
        c=rgb.reshape ( (w*h,3) ),
        alpha=0.6 )
#ax.set_thetalim ( 0,0xffffff )
#ax.set_thetalim ( 0,255 )
#ax.set_thetamin ( 0.0 )
#ax.set_thetamax ( 1.0 )
#ax.set_rlim ( 0,255 )
ax.set_rmin ( 0.0 )
ax.set_rmax ( 1.0 )
ax.set_ylim ( ymin=0, ymax=1.0 )
#ax.set_xlim ( 0,255 )
ax.set_yticks ( [] )
ax.set_xticks ( [] )

fig.show ( )
plt.show ( )
