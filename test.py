import numpy as np
import scipy.misc
import cv2
import pickle 
from matplotlib import pylab
from pylab import *
from datetime import datetime as dt
from matplotlib import pyplot as plt
from PIL import Image
import pywt
import bz2
from shutil import copyfileobj


# imgObj = Image.open("favicon.png")
# img = np.array(imgObj)
# print(img.dtype)
# # pywt
# s = dt.now()
# res_pywt = pywt.dwt2(img, "haar")
# print("pywt took:", dt.now() - s)
# print(res_pywt)
# file_pi = open('filename_pi.obj', 'wb')
# pickle.dump(res_pywt, file_pi)

file_pi2 = open('filename_pi.obj', 'rb') 
object_pi2 = pickle.load(file_pi2)


response = pywt.idwt2(object_pi2, "haar")
response = response.astype('uint8')
print(response)
res = Image.fromarray(response, "RGBA")
res.save('mys.png')
res.show()

