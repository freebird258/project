#!/usr/bin/env python

import os

L = [66,13,51,76,81,26,57,69,23]

def quick_sort(input_list):
	tmp = input_list[0]
	i = 0
	j = len(input_list) - 1
	jj = j
	if i != j:
		if tmp > input_list[j]:
			input_list[i] = input_list[j]
			input_list[j] = tmp
			i = i + 1 
			j = j -1
				if tmp  
		else:
			i = i + 1
				
	 



quick_sort(L)
