#!/usr/bin/python3
from ftplib import FTP
ftp=FTP("domainname.com")
ftp.login(user='username',passwd='password')
ftp.cwd('dirname')

def grabfile():
	filename ="filename.txt"
	localfile=open(filename,'wb')
	ftp.retrbinary('RETR '+filename, localfile.write,1024)
	ftp.quit()
	localfile.close()

def placefile():
	filename= 'filename.txt'
	ftp.storbinary('STOR '+filename,open(filename,"rb"))
	ftp.quit()
