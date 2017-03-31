# -*- coding: utf-8 -*-
import sys
import MySQLdb
import time
import datetime
import numpy as np
import pandas as pd
import tushare as ts

now_datetime = datetime.datetime.now()
now_day = now_datetime.strftime('%Y-%m-%d')
ago_nyears  = (now_datetime + datetime.timedelta(days=-365*4)).strftime('%Y-%m-%d')
def get_codename():

	today_all = ts.get_today_all()
	all_stock = today_all.loc[:,['code','name']]
	#all_stock = all_stock.drop_duplicates(['code'])

	mysql_cn= MySQLdb.connect(host='localhost',port=3306,user='root', passwd='123456', db='stock',charset="utf8")
	#all_stock.to_sql("all_stock",mysql_cn, flavor='mysql',if_exists='append',index=True,index_label="id")
	all_stock.to_sql("all_stock",mysql_cn, flavor='mysql',if_exists='fail')
	mysql_cn.close()

def get_limit(code,trade,now_day,ago_nyears):
	hist = ts.get_hist_data(str(code),start=ago_nyears,end=now_day) 
	max_value = round(hist['ma5'].max(),2)
	min_value = round(hist['ma5'].min(),2)

	if min_value > trade * 0.7:
		print "code, min_value, max_value, trade: ",code,min_value,max_value,trade

def select_code(small,big,now_day,ago_3years):
	today_all = ts.get_today_all()
	new_code = today_all[(today_all['trade']>small )& (today_all['trade']<big)].loc[:,['code','trade']]

	for num in xrange(len(new_code)):
		get_limit(new_code.iloc[num]['code'],new_code.iloc[num]['trade'],now_day,ago_nyears)
if __name__ == '__main__':
	select_code(5,10,now_day,ago_nyears)

