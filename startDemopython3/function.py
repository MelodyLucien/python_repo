#!/usr/bin/python3


'''
function

'''

def example():
	print("hello")

example()


def simple_add(num,num2):
	answer = num + num2
	print("num is",num)
	print(answer)


simple_add(3,4)
simple_add(10,20)
simple_add(100,200)

#change the order of the two parameters
simple_add(num2=900,num=100)


def simple_def(num1,num2):
	print("no defult")


def simple_def(num1,num2=10):
	print(num1,num2)


simple_def(4,5)
simple_def(4)










