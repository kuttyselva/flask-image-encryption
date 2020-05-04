import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
import pywt
import pywt.data


# Load image
# imgObj = Image.open("picture_out.png")
# original = np.array(imgObj)
original = pywt.data.camera()

# Wavelet transform of image, and plot approximation and details
titles = ['Approximation', ' Horizontal detail',
          'Vertical detail', 'Diagonal detail']
coeffs2 = pywt.dwt2(original, 'bior1.3')
LL, (LH, HL, HH) = coeffs2
fig = plt.figure(figsize=(12, 3))
for i, a in enumerate([LL, LH, HL, HH]):
    ax = fig.add_subplot(1, 4, i + 1)
    ax.imshow(a, interpolation="nearest", cmap=plt.cm.gray)
    ax.set_title(titles[i], fontsize=10)
    ax.set_xticks([])
    ax.set_yticks([])

fig.tight_layout()
plt.show()

res = pywt.idwt2(coeffs2,'bior1.3')
res = res.astype('uint8')

new_im = Image.fromarray(res,'RGBA')
# new_im.save("numpy_altered_sample2.png")
new_im.show()
# img = Image.fromarray(response, 'RGB')
# img.save('mys.png')
# img.show()