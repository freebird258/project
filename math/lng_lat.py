# -*- coding: utf-8 -*-
#!/usr/bin/env python

from scipy.optimize import fsolve 
from math import radians, cos, sin, asin, sqrt  
import random, getopt, sys
  
def getlonlat(lon,lat,lenth):
	haversine_format = '''
def haversine(x): \n
	lon1 = %s \n
	lat1 = %s  \n
	lon2 = float(x[0]) \n
	lat2 = float(x[1]) \n
	lon1, lat1, lon2, lat2 = map(radians, [lon1, lat1, lon2, lat2]) \n
	\n
	# haversine公式 \n
	dlon = lon2 - lon1  \n
	dlat = lat2 - lat1  \n
	a = sin(dlat/2)**2 + cos(lat1) * cos(lat2) * sin(dlon/2)**2  \n
	c = 2 * asin(sqrt(a))  \n
	r = 6371.004  #地球平均半径，单位为公里  \n
	
	return [c * r * 1000 - %s, 3<lat2 <53 and 73<lon2<135]''' % (lon,lat,lenth)
	exec(haversine_format)
	return fsolve(haversine, [100, 28])

if __name__ == '__main__':

	try:
		opts, args = getopt.getopt(sys.argv[1:], "h",["help"]) 
	except getopt.GetoptError as err:
		print str(err)	
		sys.exit() 

	for op, value in opts:
		if op in ("-h","--help"):
			print "------Help-----\nFunction:  find a lon and lat based existed lon/lat and lenth\nFormat:  getlonlat(lon,lat,lenth(unit:m)) e.g. 106.54637,29.592127,3000"
			sys.exit()
		else: 
			pass
#print getlonlat(*args)
	print getlonlat(106.580806,29.612838,600)

