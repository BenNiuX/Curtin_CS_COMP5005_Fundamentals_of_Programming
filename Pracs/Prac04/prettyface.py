#
# prettyface.py
#
import matplotlib.pyplot as plt
from scipy import ndimage
from scipy import misc
import numpy as np

face = misc.face()
print(np.shape(face))
face = misc.face(gray=True)
print(np.shape(face))

plt.figure('Original')
plt.imshow(face)
plt.show()

cmap_name_list = ['Greys', 'Purples', 'Blues',
        'binary', 'bone', 'pink',
        'PiYG', 'PuOr', 'bwr',
        'Pastel1', 'Paired', 'Dark2',
        'ocean', 'terrain', 'brg']

plt.figure('Gray')
plt.imshow(face, cmap=plt.cm.gray)
plt.show()

for cmap_name in cmap_name_list:
    plt.figure(f'cmap-{cmap_name}')
    plt.imshow(face, plt.get_cmap(cmap_name))
    plt.show()

plt.figure('Shift-50,50')
shifted_face = ndimage.shift(face, (50,50))
plt.imshow(shifted_face)
plt.show()

plt.figure('Rotate-30')
rotated_face = ndimage.rotate(face, 30)
plt.imshow(rotated_face)
plt.show()

plt.figure('Cropped-100:-100,100:-100')
cropped_face = face[100:-100,100:-100]
plt.imshow(cropped_face)
plt.show()

print(np.shape(face))
plt.figure('After shape')
plt.imshow(face)
plt.show()

plt.figure('Pixel-10')
pixel_face = face[::10,::10]
plt.imshow(pixel_face)
plt.show()

plt.figure('Pixel-50')
pixel_face2 = face[::50,::50]
plt.imshow(pixel_face2)
plt.show()
