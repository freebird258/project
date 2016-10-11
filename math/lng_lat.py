#!/usr/bin/python
# -*- coding: utf-8 -*-
from scipy.optimize import fsolve 
from math import radians, cos, sin, asin, sqrt  
import random
  
def haversine(lon1, lat1, lon2, lat2): # 经度1，纬度1，经度2，纬度2 （十进制度数）  
	""" 
	Calculate the great circle distance between two points  
	on the earth (specified in decimal degrees) 
	"""  
	# 将十进制度数转化为弧度  
	lon1, lat1, lon2, lat2 = map(radians, [lon1, lat1, lon2, lat2])  
	
	# haversine公式  
	dlon = lon2 - lon1   
	dlat = lat2 - lat1   
	a = sin(dlat/2)**2 + cos(lat1) * cos(lat2) * sin(dlon/2)**2  
	c = 2 * asin(sqrt(a))   
	r = 6371.004 # 地球平均半径，单位为公里  
	return c * r * 1000 

#haversine(106.54637,29.592127,106.539471,29.587887)

def f(x):
	lon1 = 106.54637
	lat1 = 29.592127
	lon2 = float(x[0])
	lat2 = float(x[1])
	lon1, lat1, lon2, lat2 = map(radians, [lon1, lat1, lon2, lat2])

    # haversine公式
	dlon = lon2 - lon1
	dlat = lat2 - lat1
	a = sin(dlat/2)**2 + cos(lat1) * cos(lat2) * sin(dlon/2)**2
	c = 2 * asin(sqrt(a))
	r = 6371.004

	return [c * r * 1000 - 500,
			3<lat2 <53 and 73<lon2<135]

result = fsolve(f, [100, 28])

print result
