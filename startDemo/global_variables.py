#!/usr/bin/python3


'''
global

'''

x = 9

def example():
#declare global variables 
	global x
	print(x)

	x+=9
	print(x)
# local variables
	s= x+90
	print(s)

example();



