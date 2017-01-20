#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import json
import urllib,urllib2
import mimetools
import mimetypes
import itertools

class MultiPartForm():
	def __init__(self):
		self.form_fields = []
		self.files = []
		self.boundary = mimetools.choose_boundary()

	def add_field(self, name, value):
		"""添加field数据到form表单"""
		self.form_fields.append((name, value))

	def add_file(self, fieldname, filename, file_obj, mimetype=None):
		"""添加文件到表单"""
		if not mimetype:
			mimetype = mimetypes.guess_type(filename)[0] or 'application/octet-stream'
		self.files.append((fieldname, filename, mimetype, file_obj.read()))
	def __str__(self):
		"""拼接form报文"""
		parts = []
		part_boundary = "--%s" % self.boundary

		# 添加fields
		parts.extend(
			[part_boundary,
			'Content-Disposition: form-data; name="%s"' %name,
			'',
			value,] for name, value in self.form_fields
			)

		# 添加要上传的files
		parts.extend(
			[part_boundary,
			'Content-Disposition: file; name="%s"; filename="%s"' % (field_name, filename),
			'Content-Type: %s' % content_type,
			'',
			body,] for field_name, filename, content_type, body in self.files
			)

		# 压平parts添加boundary终止符
		flattened = list(itertools.chain(*parts))
		flattened.append('--%s--' % self.boundary)
		flattened.append('')
		return '\r\n'.join(flattened)


def http_post(url,**kw):

	req = urllib2.Request(url)

	if kw.has_key("headers"):
		for k,v in kw["headers"].iteritems():
			req.add_header(k,v)

	if kw.has_key("values"):
		dic = kw["values"]
		for a in dic.keys():
			if type(dic[a]) == dict:
				dic[a] = json.dumps(dic[a])

	if kw["headers"]['Content-Type'] == "application/x-www-form-urlencoded":
		req.add_data(urllib.urlencode(dic))
	else:
		req.add_data(json.dumps(kw["values"]))

	try:
		response = urllib2.urlopen(req)

	except urllib2.URLError,e:
		print e and e.code and e.read()
		os._exit(-1)
	else:
		the_page = response
		return the_page

def http_get(url,**kw):

	if kw.has_key("values"):
		url_real = url + "?" + urllib.urlencode(kw["values"])
	else:
		url_real = url

	req = urllib2.Request(url_real)
	if kw.has_key("headers"):
		for k,v in kw['headers'].iteritems():
			req.add_header(k,v)
	try:
		response = urllib2.urlopen(req)
	except urllib2.URLError,e:
		print e and e.read()
	else:
		the_page = response
		return the_page


if __name__ == '__main__':
	url = "https://pay.weixin.qq.com/index.php/files/applymentnew/upload"

	filename = '/tmp/test.png'
	form = MultiPartForm()

	form.add_field('ecc_csrf_token','1111')
	form.add_field('merchantId','1111')
	form.add_field('mode','3')
	form.add_file('file', '/tmp/test.png', file_obj = open(filename))
 
	request = urllib2.Request(url)

	body = str(form)
	request.add_header('Content-type', 'multipart/form-data; boundary=%s' % form.boundary)
	request.add_header('Content-length', len(body))
	request.add_header('Cookie','33333')
	request.add_data(body)

	print(urllib2.urlopen(request).read())
