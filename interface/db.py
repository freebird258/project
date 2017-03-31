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

	def get_sql_conn(self):
		try:
			database_conn = MySQLdb.connect(host=self.host,port=self.port,user=self.user,passwd=self.password)
		except MySQLdb.Error, e:
			sys.exit(e)
		return database_conn

	def output_result(self,query):
		conn = self.get_sql_conn()
		cursor = conn.cursor()

		try:
			cursor.execute(query)
		except Exception,e:
			print Exception,":",e

		oneline =  cursor.fetchone()

		#output = open("aa",'w')  
		#output.write(json.dumps(oneline,encoding="UTF-8", ensure_ascii=False))  
		#output.close()  

		cursor.close()
		conn.close
		
		return oneline

class MerchantMysql(BasicMysql):
	def __init__(self,host,port,user,passwd,database):
		BasicMysql.__init__(self,host,port,user,passwd)
		self.database = database

	def get_merchant_passwd(self,username):
		conn = BasicMysql.get_sql_conn(self)
		cursor = conn.cursor()
		query = 'select password from %s.cb_merchant_user where username="%s";' % (self.database,username)
		try:
			cursor.execute(query)
		except Exception,e:
			print Exception,":",e
			sys.exit("load data bad")
	
		passwd_exist = cursor.fetchone()
		cursor.close()

		if passwd_exist == None:
			sys.exit("can't get merchant passwd")
		else:
			passwd = passwd_exist[0]

		return passwd	

if __name__ == '__main__':
	
	#conn = get_sql_conn("10.43.2.6",3306,"root","root")
	#print get_merchant_passwd(conn,"froad_cbank_2","4541501")
	#MerchantMysqlTest = MerchantMysql("10.43.2.6",3306,"root","root","froad_cbank_2")
	#MerchantMysqlTest.get_merchant_passwd("4541501")	
	mysql_db = {"test2":{"ip":"10.43.2.7","port":3306,"user":"root","password":"root","db":"froad_cbank_3"}}
	db = BasicMysql(host=mysql_db["test2"]["ip"],port=mysql_db["test2"]["port"],user=mysql_db["test2"]["user"],password=mysql_db["test2"]["password"])
	query = "select code from %s where mobile='%s' ORDER BY create_time desc LIMIT 1;" %(mysql_db["test2"]["db"]+".cb_sms_log",'13916455521')
	print	db.output_result(query)[0]
