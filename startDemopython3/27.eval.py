#!/usr/bin/python3

'''
eval is to parse a expression from a str to a command and run it 
then  return a result of it  
'''
list_str="[5,6,7,8,9]"

list_str=eval(list_str)

print(list_str)

print(list_str[4])

x=input("code:")

check_this_out=eval(input("code:"))

print(check_this_out)
