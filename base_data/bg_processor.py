import numpy as np
import cv2
from PIL import Image 

if __name__=='__main__':
    img=cv2.imread('FIRE_13.png', 0)
    img_copy = img.copy()
    img=cv2.imread('FIRE_13.png', 1)
    img_copy = np.array(img_copy)
    img = np.array(img)
    index = []
    for i in range(320):
      for j in range(320):
        if  img_copy[i][j] < 60:
          img_copy[i][j] = 255
        else:
          index.append((i, j))
    
    img_copy = cv2.cvtColor(img_copy,cv2.COLOR_GRAY2RGB)

  
    for tpl in index:
      i,j = tpl
      img_copy[i][j] = img[i][j]

    cv2.imshow("after",img_copy)
    cv2.waitKey(0)



