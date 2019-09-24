# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

def permute(s, start, end):
	s = list(s)
	if start == end:
		print(s)
	else:
		for i in range(start, end+1):
			s[start], s[i] = s[i], s[start]
			print(s[start], ' exchanged with ', s[i])
			permute(s, start + 1, end)
			print('return from permutation')
			s[start], s[i] = s[i], s[start]
			print(s[start], ' exchanged with ', s[i])
            
            
permute('abc', 0, 2)
