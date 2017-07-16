#!/usr/bin/python3
from ftplib import FTP
'''
ftp=FTP("linux.linuxidc.com")
ftp.login(user='www.linuxidc.com',passwd='www.linuxidc.com')
ftp.cwd('/2017年资料/1月/2日/在Ubuntu 14.04上Sublime Text无法输入中文的解决方法/')

def grabfile():
	filename ="sublime-imfix-master.zip"
	localfile=open(filename,'wb')
	ftp.retrbinary('RETR '+filename, localfile.write,1024)
	ftp.quit()
	localfile.close()

def placefile():
	filename= 'filename.txt'
	ftp.storbinary('STOR '+filename,open(filename,"rb"))
	ftp.quit()


grabfile()

print("over!")
'''


ftp=FTP("www.python.org")
ftp.login(user='www.linuxidc.com',passwd='www.linuxidc.com')
ftp.cwd('/ftp/')

def grabfile():
	filename ="README.txt"
	localfile=open(filename,'wb')
	ftp.retrbinary('RETR '+filename, localfile.write,1024)
	ftp.quit()
	localfile.close()

def placefile():
	filename= 'filename.txt'
	ftp.storbinary('STOR '+filename,open(filename,"rb"))
	ftp.quit()

grabfile()


print("over!")
