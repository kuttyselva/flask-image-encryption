import numpy as np
import scipy.misc
import cv2
# import pylab
from matplotlib import pylab
from pylab import *
from datetime import datetime as dt
from matplotlib import pyplot as plt
from PIL import Image
import pywt


def show(data):
    pylab.jet()
    pylab.imshow(data)
    pylab.colorbar()
    pylab.show()
    pylab.clf()


imgObj = Image.open("picture_out.png")
img = np.array(imgObj)
print(img.dtype)
# pywt
s = dt.now()
res_pywt = pywt.dwt2(img, "haar")
print("pywt took:", dt.now() - s)
# show(res_pywt[0])
img = Image.fromarray(res_pywt[0], 'RGBA')
img.save('my.png')
img.show()

response = pywt.idwt2(res_pywt, "haar")
response = response.astype('uint8')
# print(response)

res = Image.fromarray(response, "RGBA")
res.save('mys.png')
res.show()

