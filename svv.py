# -*- coding: utf-8 -*-
"""
Created on Thu Feb  9 11:17:40 2017

@author: Alanna
"""

from pylab import *
from PIL import Image

im = Image.open('RilakummaWallpaper.JPG').convert('L')
w,h = im.size()
data = array(im.getdata()).reshape((w,h))
