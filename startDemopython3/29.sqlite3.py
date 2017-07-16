#!/usr/bin/python3
'''
go http://sqlitebrowser.org/  and get sqlite3 broswer 
'''
import sqlite3
import time
import datetime
import random
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
# from matplotlib import style

# style.use('fivethirtyeight')

conn = sqlite3.connect("my.db")
c = conn.cursor()

def create_table():
	c.execute('CREATE TABLE IF NOT EXISTS stuffToPlot(unix REAL,datastamp TEXT,keyword TEXT,value REAL)')

def data_insert():
	c.execute("INSERT INTO stuffToPlot VALUES(1451255552,'2017-05-22','Python',8)")
	conn.commit()
	c.close()
	conn.close()

def dynamic_data_entry():
	unix=time.time()
	date=str(datetime.datetime.fromtimestamp(unix).strftime('%Y-%m-%d %H-%M-%S'))
	keyword='Python'
	value=random.randrange(0,10)
	c.execute("INSERT INTO stuffToPlot (unix,datastamp,keyword,value) VALUES (?,?,?,?)",(unix,date,keyword,value))
	conn.commit()

def readFromDb():
	c.execute('SELECT * FROM stuffToPlot WHERE value IN (4,9)')
	data=c.fetchall()
	for row in data:
		print(row[1])

def graph_data():
	c.execute('SELECT unix,value FROM stuffToPlot')
	dates=[]
	values=[]
	data=c.fetchall()
	for row in data:
		dates.append(row[0])
		values.append(row[1])
	plt.plot(dates,values)
	plt.show()

def del_update():
	c.execute('SELECT * FROM stuffToPlot')
	data=c.fetchall()
	for row in data:
		print(row)

	print("#"*50)

	c.execute("UPDATE stuffToPlot SET value = 100 WHERE value=3")
	conn.commit()

	c.execute('SELECT * FROM stuffToPlot')
	data=c.fetchall()
	for row in data:
		print(row)

# create_table()
# #data_insert()
# for x in range(1,20):
# 	dynamic_data_entry()
# 	time.sleep(1)


#readFromDb()
#graph_data()
del_update()
c.close()
conn.close()
