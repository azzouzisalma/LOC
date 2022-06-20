#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr  6 16:25:01 2022

@author: sazzouzi
"""

import numpy as np
from PIL import Image, ImageOps
import matplotlib.pyplot as plt
from matplotlib import image 


im_gray = (Image.open('im2.jpeg'))
img_gray = ImageOps.grayscale(im_gray)
print(img_gray.mode)
img_gray = np.array(img_gray)
#%%
print(type(im_gray))
a= im_gray[:,:,1]
# <class 'numpy.ndarray'>
plt.figure
plt.imshow(a)
a_ligne = a.reshape(161*215)

#%%
def de2bin(int):
    b= []
    while int!=0:
        b.insert(0,int%2)   
        int = int //2
    return b

sequence = []
for k in range(len(a_ligne)):
    bin = de2bin(a_ligne[k])
    sequence= sequence+ bin
