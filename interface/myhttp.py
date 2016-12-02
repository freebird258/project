#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import json
import urllib,urllib2


def http_post(url,**kw):

	req = urllib2.Request(url)

	if kw.has_key("headers"):
		for k,v in headers.iteritems():
			req.add_header(k,v)

	if kw.has_key("values"):
		req.add_data(urllib.urlencode(kw["values"]))
		#req.add_data(json.dumps(kw["values"])) ##str
	try:
		#req = urllib2.Request(url, data,headers)
		response = urllib2.urlopen(req)
	except urllib2.URLError,e:
		print e
		print e.code
		print e.read()
		os._exit(-1)
	else:
		the_page = response.read()
		print the_page

def http_get(url,**kw):

	if kw.has_key("values"):
		url_real = url + "?" + urllib.urlencode(kw["values"])
	else:
		url_real = url

	req = urllib2.Request(url_real)
	if kw.has_key("headers"):
		for k,v in headers.iteritems():
			req.add_header(k,v)
	try:
		response = urllib2.urlopen(req)
	except urllib2.URLError,e:
		print e
		#print e.read()
	else:
		the_page = response.read()
		print the_page


if __name__ == '__main__':
#	url = "http://127.0.0.1:8000/merchant/handle_post/"
#	headers = {"Referer": "https://test1.ubank365.com/chongqing/admin/merchant/index.htm", "Content-Type": "application/json"}
#	values = {'staff': 'test',"aa":"11"}
#	http_post(url,headers,values)
	url = "http://10.24.242.41:8000"
	#http_get(url)
	values = {"greeting":"Salutations"}
	#http_post(url,headers=headers,values=values)
	http_post(url,values=values)

