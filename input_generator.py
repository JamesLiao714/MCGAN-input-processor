from PIL import Image
import numpy as np
import os
'''
os.mkdir('WATER')
os.mkdir('WATER/A')
os.mkdir('WATER/B')
os.mkdir('WATER/A/train')
os.mkdir('WATER/B/train')
os.mkdir('WATER/A/test')
os.mkdir('WATER/B/test')
'''


def save_input(s, fn):
  o = Image.fromarray(s.astype('uint8'), 'RGB')
  o.save('WATER/B/train/' + fn)

l1 = np.array(Image.open("WATER_0.png"))
save_input(l1, "WATER_0.png")
l2 = np.array(Image.open("WATER_4.png"))
save_input(l2, "WATER_4.png")
l3 = np.array(Image.open("WATER_17.png"))
save_input(l3, "WATER_17.png")
l4 = np.array(Image.open("WATER_19.png"))
save_input(l4, "WATER_19.png")
l5 = np.array(Image.open("WATER_22.png"))
save_input(l5, "WATER_22.png")

base = np.array(Image.open("base.png"))



white = np.zeros((64,64,3))
for i in range(64):
  for j in range(64):
    white[i][j] = [255, 255, 255]


llst = []
llist = [0, 4, 17, 19, 22]

inp = np.zeros((64, 5*64, 3))
inp[:, :64] = l1
inp[:, 64:64*2] = l2
inp[:, 64*2:64*3] = l3
inp[:, 64*3:64*4] = l4
inp[:, 64*4:64*5] = l5

userinp = Image.fromarray(inp.astype('uint8'), 'RGB')
userinp.save('check1.png')



out = np.zeros(base.shape)
j = 0
for i in range(0, 26):
  if i in llist:
    out[:, 64*i:64*(i+1)] = inp[:, 64*j: 64*(j+1)]
    j += 1
  else:
    out[:, 64*i:64*(i+1)] = white


userout = Image.fromarray(out.astype('uint8'), 'RGB')
userout.save('WATER/A/test/WATER.png')







