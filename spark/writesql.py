#!/usr/bin/env python
# encoding: utf-8

import os
import sys
import time
import random
import uuid
import datetime

path = os.path.split(os.path.realpath(__file__))[0]
sys.path.append(os.path.join(path,"../"))
from interface.db import BasicMysql

class LoopDone(Exception):pass


class CreateDB(object):
	def __init__(self,start_time,end_time,product_name_dict):
		self.start_time_stamp = time.mktime(time.strptime(start_time,"%Y-%m-%d %H:%M:%S"))
		self.end_time_stamp = time.mktime(time.strptime(end_time,"%Y-%m-%d %H:%M:%S"))
		print self.end_time_stamp - self.start_time_stamp
		self.product_name_dict = product_name_dict

	def carry_db(self,db):
		start_stamp = self.start_time_stamp
		num = 1
		db_values = "INSERT INTO spark_test.product VALUES "

		filename = "/tmp/1.txt"
		myfile = file(filename,"w+")
		try:
			while True:
				price_c = random.randint(20,30)
				for i in xrange(1,price_c):
					start_stamp = start_stamp + random.randint(0,10)
					pay_time = time.strftime("%Y-%m-%d %H:%M:%S",time.localtime(start_stamp))
					product_name = random.choice(self.product_name_dict.keys())
					price = random.randint(100,150)
#					line = "%s,%s,%s,%s,%s\n" % (num,product_name,product_name_dict[product_name],pay_time,price)
#					myfile.write(line)
					if num % 40000 == 0:
						db_values = db_values + "('%s','%s','%s','%s','%s') " % (num,product_name,product_name_dict[product_name],pay_time,price)
						db.exec_insert(db_values)
						db_values = "INSERT INTO spark_test.product VALUES "
					else:
						db_values = db_values + "('%s','%s','%s','%s','%s')," % (num,product_name,product_name_dict[product_name],pay_time,price)
					if num == 10000000: raise LoopDone
					num = num + 1
		except LoopDone:
			print "Done"


if __name__ == "__main__":
	product_name_dict = {"rice":"MMRICE0001","peach":"MMPEACH012","Pear":"MMPEAR9871","Banana":"MMBANANA34","plum":"MMPLUM7632","orange":"MMORANGE9"}

	starttime = datetime.datetime.now()

#	filename = "/tmp/1.txt"
#	myfile = file(filename,"w+")

	db = BasicMysql(host="127.0.0.1",port=3306,user="root",password="123456")
	creatdb = CreateDB("2014-01-01 00:00:00","2015-03-01 00:00:00",product_name_dict)
	creatdb.carry_db(db)

#	myfile.close()
#
#	query = "load data local infile '%s' replace into table spark_test.product  fields terminated by ',';" % filename
#	db.exec_insert(query)

	endtime = datetime.datetime.now()
	print endtime - starttime
