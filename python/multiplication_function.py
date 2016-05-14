"""
	This codewar - kyu 7 - seems challenging
	1.) review binary numbers
	2.) look at bitwise operators
"""

def my_climb(n):
	if n == 1:
		return [1]
	else:
		return my_climb(int(n/2)) + [n]


####### test
print my_climb(5)