# Text to grayscale image conversion 
# -- Assuming they are in order
# Author: Gazi Inkiyad

#%% 
import glob
import numpy as np
import os
import matplotlib.pyplot as plt
import csv

files = glob.glob('../Data/Sorted/*lymphocyte*.txt')

for filename in files:
    
    pixel = []

    with open(filename, 'r') as file: 
        next(file) 
        for row in file:
            ycoor, xcoor, intensity = row.split('	')  
            pixel.append([int(ycoor),int(xcoor),float(intensity)])
            pass
        pass

    pixel = np.asarray(pixel)
    print(len(pixel))

    ylength = len(np.argwhere(np.diff(pixel[:,0])>1))+1
    xlength = int(len(pixel[:,0])/ylength)

    GrayImg = pixel[:,2].reshape((ylength,xlength)) 
    GrayImg = np.transpose(GrayImg)
    plt.imshow(GrayImg, cmap='jet')
    plt.show()
    


    pass






#%%
