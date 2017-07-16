#!/usr/bin/python3
import socket
import sys
from _thread import *


def thread_client(conn):
	conn.send(str.encode("Welcome,type your info\n"))

	while True:
		data=conn.recv(2048)
		reply="server output: "+ data.decode('utf-8')
		if not data:
			break
		conn.sendall(str.encode(reply))


host=''
port=5555
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

try:
	s.bind((host,port))
except Exception as e:
	print(str(e))

s.listen(5)
print("waiting for a connection")

while True:

	conn,addr=s.accept()

	start_new_thread(thread_client,(conn,))

	print("connected to:", addr[0],addr[1])