# -*- coding: utf-8 -*-
"""
Created on Thu Feb  9 00:29:54 2017

@author: Alanna
"""
#imports nessary imports
from pylab import *


#opens and reads text file  
f = open('thegiver.txt','r')
data = f.read().decode('utf-8',errors = 'ignore')

f.close()

t ={}
p =data[0]
for i in range(1,len(data)):
    if data[i] in t:
        c = data[i]
        if p in t:
            t[p].append(c)
        else:
            t[p] = [c]
        p = c

c = 'H'
gibberish = c
for i in range(5000):
    c = choice(t(c))
    gibberish += c
    