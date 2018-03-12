import cv2
import numpy as np
from matplotlib import pyplot as plt

filename = ['Cameraman', 'SEM256_256']
img1 = cv2.imread(filename[0]+'.pgm',0)
img2 = cv2.imread(filename[1]+'.pgm',0)

equ1 = cv2.equalizeHist(img1)
equ2 = cv2.equalizeHist(img2)

#stacking images side-by-side
res1 = np.hstack((img1,equ1))
res2 = np.hstack((img2,equ2))

hist1,bins1 = np.histogram(equ1.flatten(),256,[0,256])
hist2,bins2 = np.histogram(equ2.flatten(),256,[0,256])

cdf1 = hist1.cumsum()
cdf_normalized1 = cdf1 * hist1.max()/ cdf1.max()

cdf2 = hist2.cumsum()
cdf_normalized2 = cdf2 * hist2.max()/ cdf2.max()

# first figure
plt.figure(filename[0])
plt.title(filename[0])
# plt.plot(cdf_normalized1, color = 'b')
plt.hist(img1.flatten(),256,[0,256], color = 'r')

plt.figure(filename[1])
plt.title(filename[1])
# plt.plot(cdf_normalized2, color = 'b')
plt.hist(img2.flatten(),256,[0,256], color = 'r')

plt.xlim([0,256])
plt.legend(('cdf','histogram'), loc = 'upper left')
plt.show()
cv2.imwrite(filename[0]+'_out.pgm',res1)
cv2.imwrite(filename[1]+'_out.pgm',res2)