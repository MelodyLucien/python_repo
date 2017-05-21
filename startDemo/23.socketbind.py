#!/usr/bin/python3
import socket

host=''
port=5555
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

try:
	s.bind((host,port))
except Exception as e:
	print(str(e))


s.listen()

conn,addr=s.accept()

print("connected to:", addr[0],addr[1])