# -*- coding: utf-8 -*-
"""
Lecture 6

@author: Alanna
"""

from pylab import *
import urllib.request as url

f = url.urlopen('https://www.binghamton.edu/')

# data = f.readlines()

c = 0

for line in f:
    if str('binghamton') in line.lower():
        c += 1
        print (line)
f.close()

print (c)
