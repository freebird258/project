#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import sys
import MySQLdb
import numpy as np
import pandas as pd
import tushare as ts

path = os.path.split(os.path.realpath(__file__))[0]
sys.path.append(os.path.join(path,"../"))
from misc.mydb import MySql

def get_codename(today_all):

	all_stock = today_all.loc[:,['code','name']]

	all_stock = all_stock.drop_duplicates(['code'])

	mysql_cn= MySQLdb.connect(host='localhost',port=3306,user='root', passwd='123456', db='stock',charset="utf8")

	all_stock.to_sql("all_stock",mysql_cn, flavor='mysql',if_exists='append')
	mysql_cn.close()

if __name__ == '__main__':

	today_all = ts.get_today_all()
	get_codename(today_all)
