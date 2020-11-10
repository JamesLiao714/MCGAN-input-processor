import cv2
import numpy as np
from PIL import Image
import os

img = cv2.imread('SMOKE_0.png')
res = cv2.resize(img, dsize=(320, 320), interpolation=cv2.INTER_CUBIC)
cv2.imwrite('SMOKE_0.png',res)
'''
l1 = np.array(Image.open("SMOKE_22.png"))
print(l1.shape)
for i in range(64):
  for j in range(64):
      #print(l1[i][j])
      if [0, 0, 0] in l1[i][j]:
          l1[i][j] = [255, 255, 255]
s = Image.fromarray(l1.astype('uint8'), 'RGB')
s.save('SMOKE_22.png')

print('finish')
'''

