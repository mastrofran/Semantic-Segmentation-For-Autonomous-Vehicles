from PIL import Image
import numpy as np
import os

root_dir = '/home/mil/haqishen/data/TDD/'
img_dir = root_dir + 'images/' # data
lbl_dir = root_dir + 'labels/' # label
list_file = root_dir + 'train.txt'

files = []
with open(list_file,'r') as reader:
  for line in reader.readlines():
    files.append(line.strip('\n'))
print(len(files))
id = 1
for f in files:
  if 'flip' in f:
    continue

  Image.open(img_dir+f+'.png').transpose(Image.FLIP_LEFT_RIGHT).save(img_dir+f.split('.')[0]+'_flip.png', 'PNG')
  Image.open(lbl_dir+f+'.png').transpose(Image.FLIP_LEFT_RIGHT).save(lbl_dir+f.split('.')[0]+'_flip.png', 'PNG')
 
  print(id)
  id += 1
