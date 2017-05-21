#!/usr/bin/python3
import urllib.request
import urllib.parse

#x = urllib.request.urlopen("http://www.baidu.com")

#print(x.read())


'''
#get method

url="http://music.baidu.com/search"

values={"key":"Ed Sheeran"}

data = urllib.parse.urlencode(values)

data = data.encode('utf-8')

req = urllib.request.Request(url,data)

resp = urllib.request.urlopen(req)

print(resp.read())

'''

try:
	url="http://music.baidu.com"
	headers={}
	headers['User-Agent'] = "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:53.0) Gecko/20100101 Firefox/53.0"
	req = urllib.request.Request(url,headers=headers)
	resp=urllib.request.urlopen(req)
	respData= resp.read()

	saveFile = open("html.txt",'w')
	saveFile.write(str(respData))

	saveFile.flush()
	saveFile.close()
except Exception as e:
	print(str(e))













