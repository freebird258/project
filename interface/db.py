#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os,sys
import MySQLdb,pymongo
import json

class BasicMysql:
	def __init__(self,**kw):
		self.host = kw['host']
		self.port = kw['port']
		self.user = kw['user']
		self.password = kw['password']

		try:
			database_conn = MySQLdb.connect(host=self.host,port=self.port,user=self.user,passwd=self.password,local_infile = 1,charset="utf8")
		except MySQLdb.Error, e:
			sys.exit(e)
		self.conn = database_conn

	def exec_insert(self,query):
		conn = self.conn
		cursor = conn.cursor()

		try:
			cursor.execute(query)
		except Exception,e:
			print Exception,":",e

		conn.commit()
		cursor.close()
		
#		return oneline

	def __exit__(self):
		try:
			self.conn.close
		except Exception,e:
			 print Exception,":",e

if __name__ == '__main__':
	pass	
