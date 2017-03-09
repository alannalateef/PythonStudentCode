# -*- coding: utf-8 -*-
"""
Created on Tue Feb 21 02:57:53 2017

@author: Alanna
"""
import numpy as np  
import matplotlib.pyplot as pp  
import pandas as pd
from PIL import Image  
from PIL import ImageFilter  
pp.style.use('dark_background')

open('table.csv','r').readlines()

#import the price data into a Pandas DataFrame using read_csv function
#the 1st col contains trading date so tell 
#Pandas to look for dates & parse them into the correct datetime64 data type

s = pd.read_csv('table.csv',parse_dates=['Date']) 

#inspect the data types of the s DataFrame
#Pandas automatically parsed them into the correct data types

s.dtypes

#sort values by date
s = s.sort_values(by='Date')


#trading date the index for the Pandas DataFrame 
s.set_index('Date',inplace=True) 


#plot the closing price of s over the entire date range in DataFrame
s['Close'].plot(figsize=(15, 15)) 
 
#saves the rolling mean data , window is the number of points for the (20,6)
dis = s.rolling(window = 20, min_periods = 1).mean()

#plot with closing price
dis['Close'].plot(figsize=(15, 15)) 

#opens image
im = Image.open('hw3graph.jpeg').convert('L')

#filters image, to use multiples on top of eachother ref last filtered image
im2 = im.filter(ImageFilter.BLUR)
im3 = im2.filter(ImageFilter.CONTOUR)
im4 = im3.filter(ImageFilter.DETAIL)
im5 = im4.filter(ImageFilter.EMBOSS)

