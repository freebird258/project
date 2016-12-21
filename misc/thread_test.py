#!/usr/bin/env python
# -*- coding:utf-8 -*-

import time
import threading
 
class MyThread(threading.Thread):
	def __init__(self,parm):
		threading.Thread.__init__(self)
		self.parm = parm

	def run(self):
		for i in xrange(5):
			print 'thread {}, @number: {}, {}'.format(self.name, self.parm,i)
 
def exec_thread(p):
	threads = [MyThread(i) for i in xrange(p)]

	for t in threads:
		t.start()
 
	for t in threads:
		t.join()

 
if __name__ == '__main__':
	exec_thread(5)
