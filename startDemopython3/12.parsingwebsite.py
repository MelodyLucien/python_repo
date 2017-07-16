#!/usr/bin/python3
import urllib.request
import urllib.parse
import re

#x = urllib.request.urlopen("http://www.baidu.com")

#print(x.read())



#get method

url="http://music.baidu.com/search"

values={"key":"Ed Sheeran"}

data = urllib.parse.urlencode(values)

data = data.encode('utf-8')


req = urllib.request.Request(url,data)

resp = urllib.request.urlopen(req)


#paragraphs=re.findall(r'<p>(.*?)</p>',str(resp.read()))
htmldata=resp.read();

#herfs=re.findall(r'href=\"/song/\d*\".*data-songdata=\"\{.*\}',str(htmldata))

#herfs=re.findall(r'\{\s*"id"\:\s*"\d*"\s*\}',str(htmldata))


herfs=re.findall(r'data-songdata=\\\'\{\s*"id"\:\s*"\d*"\s*\}\\\'',str(htmldata))

print(herfs)
















