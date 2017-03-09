# -*- coding: utf-8 -*-
"""
Created on Thu Feb  9 10:31:39 2017

@author: Alanna
"""

from PIL import Image
im = Image.open('RilakummaWallpaper.JPG')
for angle in range(0,360,20):
    im.rotate(angle,expand = True).save(str(angle)+ '.jpg')