#!/usr/bin/env python
# encoding: utf-8

import time
import random
import uuid


if __name__ == "__main__":
	start_time_stamp = time.mktime(time.strptime("2014-01-01 00:00:00","%Y-%m-%d %H:%M:%S"))
	end_time_stamp = time.mktime(time.strptime("2015-03-01 00:00:00","%Y-%m-%d %H:%M:%S"))
    
	product_name_list = ["苹果","橘子","香蕉","大米","小米","鱼","肉","牛肉"]

	myfile = file("/tmp/1.txt","w+")
	for i in xrange(0,3):
		my_stamp = random.randint(int(start_time_stamp), int(end_time_stamp))
		pay_time = time.strftime("%Y-%m-%d %H:%M:%S",time.localtime(my_stamp))

		product_name = random.choice(product_name_list)
		product_id = uuid.uuid1()
		price = random.randint(100,150)
		line = ",%s,%s,%s,%s\n" % (product_name,product_id,pay_time,price)
		myfile.write(line)
	myfile.close()

