# -*- coding: utf-8 -*-
# -*- coding: utf-8 -*-
"""
Created on Thu Sep  5 15:15:31 2019

@author: Jeremy La Porte
Release : V1.0
Outline recognition of pictures and "draw" on a .doc file the outlines with keyboard characters. (Put the writing size to '1' in word)
"""

import matplotlib.image as mpimg
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.pyplot import figure
import os

import sys
np.set_printoptions(threshold=sys.maxsize)



NAME = ''
img = mpimg.imread("image/" + NAME + ".png")
if img.dtype == np.float32: # Si le résultat n'est pas un tableau d'entiers
    img = (img * 255).astype(np.uint8)

K_mid = 20
K_ext = 20
light = 0.0001
med = 0.001
dark = 0.01
surface = 2024/(img.shape[0]*img.shape[1])


print('img shape :',img.shape)
print('nombre de pixels :',img.shape[0]*img.shape[1])

P = []
fichier = open(NAME + 'x' + '.doc', "w")
x = []
y = []
XC = []
YC = []
C = []
A = np.eye(int(img.shape[0]),int(img.shape[1]))
for i in range(0,img.shape[0]-1):
        ### Afficher le pourcentage ======================

        if i%(int((img.shape[0]-1)/50)) == 0:
            print(int(100*i/(img.shape[0]-1)),'%')
        ### ============================================
        ### Calculer diff ==============================
        for j in range(0,img.shape[1]-1):

            imlistA = img[i,j]
            imlistB = img[i,j+1]
            imlistC = img[i+1,j]
            imlistD = img[i+1,j+1]
            deltaB = abs( int(imlistA[0]) - int(imlistB[0]) + int(imlistA[1]) 
            - int(imlistB[1]) + int(imlistA[2]) - int(imlistB[2]))
            deltaC = abs( int(imlistA[0]) - int(imlistC[0]) + int(imlistA[1]) 
            - int(imlistC[1]) + int(imlistA[2]) - int(imlistC[2]))
            deltaD = abs( int(imlistA[0]) - int(imlistD[0]) + int(imlistA[1]) 
            - int(imlistD[1]) + int(imlistA[2]) - int(imlistD[2]))
        ### ===================================================================
            Color = (img[i,j]/255)
            XC.append((j+j+1)*0.5)
            YC.append(-i)
            C.append(Color)
            
            if (j > 0.2*img.shape[1]) and (j < 0.8*img.shape[1]) and (i > 0.2*img.shape[0]) and (i < 0.8*img.shape[0]):
                k = K_mid
            else:
                k = K_ext
            if (deltaB >= k) or (deltaC >= k) or (deltaD >= k):
                
                x.append((j+j+1)*0.5)
                y.append(-i)
                
                
                if Color[0] + Color[1]+ Color[2] <= 1.5:
                    if j!= img.shape[1]-2:
                        fichier.write('#')
                    else:
                        fichier.write('#\n')
                else:
                    if j!= img.shape[1]-2:
                        fichier.write('*')
                    else:
                        fichier.write('*\n')
                    
            else:
                if Color[0] + Color[1]+ Color[2] <= 1.2:
                    if j != img.shape[1]-2:
                        fichier.write('_')
                    else:
                        fichier.write('_\n')
                else:
                    if j != img.shape[1]-2:
                        fichier.write(' ')
                    else:
                        fichier.write(' \n')
                    
                    
                    
# plt.scatter(XC,YC,c= C,s = surface)
plt.scatter(x,y,c= 'r',s = surface)


fichier.close()








