from PIL import Image
import numpy as np
from os import path
import os
import cv2



#create directory
f_name = str(input('please input file name: '))
if not path.exists(f_name):
  os.mkdir(f_name)
  os.mkdir(f_name + '/A')
  os.mkdir(f_name + '/B')
  os.mkdir(f_name + '/A/train')
  os.mkdir(f_name + '/B/train')
  os.mkdir(f_name + '/A/test')
  os.mkdir(f_name + '/B/test')

index = []

for w in range(5):
  index.append(str(ord(input('please input index of pic[' + str(w) + ']: ')) - ord('A')))
  whiting = np.array(Image.open('base_data/' + f_name + '_' + index[w]+'.png'))
  # white the image
  grey_img = cv2.imread('base_data/' + f_name + '_' + index[w]+'.png', 0)
  img_copy = grey_img.copy()
  color_img = cv2.imread('base_data/' + f_name + '_' + index[w]+'.png', 1)
  img_copy = np.array(img_copy)
  color_img = np.array(color_img)
  color_buff = []
  for i in range(320):
    for j in range(320):
      if  img_copy[i][j] < 60:
        img_copy[i][j] = 255
      else:
        color_buff.append((i, j))
  
  img_copy = cv2.cvtColor(img_copy,cv2.COLOR_GRAY2RGB)
  

  for tpl in color_buff:
    i,j = tpl
    img_copy[i][j] = color_img[i][j]

  cv2.imwrite('data2/' + f_name + '_' + index[w]+'.png', img_copy) 
  #s = Image.fromarray(img_copy.astype('uint8'), 'RGB')
  #s.save('data2/' + f_name + '_' + index[w]+'.png') 
  print('finish_whiting picture ')
  #resize to 64*64
  img = cv2.imread('data2/' + f_name + '_' + index[w]+'.png')
  res = cv2.resize(img, dsize=(64, 64), interpolation=cv2.INTER_CUBIC)
  cv2.imwrite('data2/' + f_name + '_' + index[w]+'.png', res)
  


def save_input(s, fn):
  o = Image.fromarray(s.astype('uint8'), 'RGB')
  o.save(f_name + '/B/train/' + fn)

l1 = np.array(Image.open('data2/' + f_name + '_' + index[0] + '.png'))
save_input(l1,  f_name + '_' + index[0]+'.png')
l2 = np.array(Image.open('data2/' + f_name + '_' + index[1] + '.png'))
save_input(l2,  f_name + '_' + index[1]+'.png')
l3 = np.array(Image.open('data2/' + f_name + '_' + index[2] + '.png'))
save_input(l3,  f_name + '_' + index[2]+'.png')
l4 = np.array(Image.open('data2/' + f_name + '_' + index[3] + '.png'))
save_input(l4,  f_name + '_' + index[3]+'.png')
l5 = np.array(Image.open('data2/' + f_name + '_' + index[4] + '.png'))
save_input(l5,  f_name + '_' + index[4] +'.png')

#save b/test base data
base = np.array(Image.open("base_data/base.png"))
btest = Image.fromarray(base.astype('uint8'), 'RGB')
btest.save(f_name + '/B/test/' + f_name + '.png')


white = np.zeros((64,64,3))
for i in range(64):
  for j in range(64):
    white[i][j] = [255, 255, 255]



inp = np.zeros((64, 5*64, 3))
inp[:, :64] = l1
inp[:, 64:64*2] = l2
inp[:, 64*2:64*3] = l3
inp[:, 64*3:64*4] = l4
inp[:, 64*4:64*5] = l5


out = np.zeros(base.shape)
j = 0
for i in range(0, 26):
  if str(i) in index:
    i = int(i)
    out[:, 64*i:64*(i+1)] = inp[:, 64*j: 64*(j+1)]
    j += 1
  else:
    out[:, 64*int(i):64*(int(i)+1)] = white

userout = Image.fromarray(out.astype('uint8'), 'RGB')
userout.save(f_name + '/A/test/' + f_name + '.png')


for i in index:
  temp = np.copy(out)
  temp[:, 64*int(i):64*(int(i)+1)] = white
  
  s = Image.fromarray(temp.astype('uint8'), 'RGB')
  s.save(f_name + '/A/train/' + f_name + '_' +  str(i) + '.png')


print('finish')


