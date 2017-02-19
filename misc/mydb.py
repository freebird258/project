#!/usr/bin/env python
# -*- coding:utf-8 -*-

import os,sys
import MySQLdb,pymongo
import json

class MySql(object):
	def __init__(self,host,port,user,passwd,db):
		try:
			database_conn = MySQLdb.connect(host=host,port=port,user=user,passwd=passwd,db=db,charset="utf8")
		except:
			sys.exit("bad mysql and exit")

		self.conn = database_conn

	def __del__(self):
		print "del database_conn"
		self.conn.close
			
	def exec_inser(self,query):
		conn = self.conn
		cursor = conn.cursor()

		try:
			cursor.execute(query)
		except Exception,e:
			print Exception,":",e

		conn.commit()
		cursor.close()

	def exec_insermany(self,query,data):
		conn = self.conn
		cursor = conn.cursor()

		try:
			cursor.executemany(query,data)
		except Exception,e:
			print Exception,":",e

		conn.commit()
		cursor.close()

		
if __name__ == '__main__':
	
	T = [(1,"b","人"),(2,"d","生")]
	db = MySql("127.0.0.1",3306,"root","123456","stock")
	query = "insert into all_stock(id,code,name) values(%s,%s,%s)"
	db.exec_insermany(query,T)
