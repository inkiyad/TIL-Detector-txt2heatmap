# Sorting text or csv files data by first 2 columns basis
# -- Assuming columns are easily distinguishable
# Author: Gazi Inkiyad

#%%
import glob
import numpy as np 
import csv
import matplotlib.pyplot as plt
import os

os.chdir('../Data/Unsorted/')

files = glob.glob('*.txt')

for filename in files:

    pixel = []
    savename = filename.split('.txt')[0]
    savepath = '../../Outputs/'

    with open(filename, 'r') as file:
        for row in file:
            ycoor, xcoor, intensity = row.split(' ')
            pixel.append([int(ycoor), int(xcoor), float(intensity)])
            pass
        pass

    pixel = np.asarray(pixel)
    pixelsort = np.lexsort((pixel[:,1], pixel[:,0]))

    pixel = pixel[pixelsort]

    ylength = len(np.argwhere(np.diff(pixel[:,0])>1))+1
    xlength = int(len(pixel[:,0])/ylength)

    GrayImg = pixel[:,2].reshape((ylength,xlength))
    GrayImg = np.transpose(GrayImg)
    GrayImg = np.uint8(GrayImg*255)

    os.chdir(savepath)
    plt.imsave(savename, GrayImg, cmap='jet', format='jpg')

    plt.imshow(GrayImg, cmap='jet')
    plt.xticks([]); plt.yticks([])

    plt.show()


    pass

#%%
