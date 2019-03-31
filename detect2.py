from model_api import UNET
import cv2
import numpy as np
img=cv2.imread('0.jpg')
net = UNET()
out = net.predict(img)
print(out)
out*=255
cv2.imwrite('out.jpg', out)
img=cv2.imread('out.jpg')
'''
print(img.shape)
for i in range(464):
    for j in range(464):
        if not (i> 132 and i<332 and j>132 and j<332):
            img[i,j]=0'''
cv2.imshow('frame', img)
cv2.waitKey(1)
cv2.imwrite('out1.jpg', img)