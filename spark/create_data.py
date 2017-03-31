#!/usr/bin/env python
# encoding: utf-8

import os
import sys
import time
import random
import uuid

path = os.path.split(os.path.realpath(__file__))[0]
sys.path.append(os.path.join(path,"../"))
from interface.db import BasicMysql


if __name__ == "__main__":
	start_time_stamp = time.mktime(time.strptime("2014-01-01 00:00:00","%Y-%m-%d %H:%M:%S"))
	end_time_stamp = time.mktime(time.strptime("2015-03-01 00:00:00","%Y-%m-%d %H:%M:%S"))
    
	product_name_list = ["rice","peach","Pear","Banana","plum","orange"]

	filename = "/tmp/1.txt"
	myfile = file(filename,"w+")
	for i in xrange(1,1000):
		my_stamp = random.randint(int(start_time_stamp), int(end_time_stamp))
		pay_time = time.strftime("%Y-%m-%d %H:%M:%S",time.localtime(my_stamp))

		product_name = random.choice(product_name_list)
		product_id = uuid.uuid1()
		price = random.randint(100,150)
		line = "%s,%s,%s,%s,%s\n" % (i,product_name,product_id,pay_time,price)
		myfile.write(line)
	myfile.close()

	db = BasicMysql(host="127.0.0.1",port=3306,user="root",password="123456")
	query = "load data local infile '%s' replace into table spark_test.product  fields terminated by ',';" % filename
	db.exec_insert(query)

