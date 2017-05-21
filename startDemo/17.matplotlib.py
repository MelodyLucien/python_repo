#!/usr/bin/python3

# pip3 install matplotlib
from matplotlib import pyplot as plt

#import data from net or file
x=[5,6,7,8]
y=[7,8,9,1]

'''
x2=[4,3,2,1]
y2=[1,2,3,4]

plt.plot(x,y,'r',linewidth=5,label='today')
plt.plot(x2,y2,'g',linewidth=10,label='yestoday')

plt.scatter(x,y,color='r',label='today')
plt.scatter(x2,y2,color='g',label='yestoday')
'''

plt.bar(x,y,color='r',label='today')
#plt.bar(x2,y2,color='g',label='yestoday')


#add labels
plt.grid(True,color='k')
plt.title("My Chart")
plt.ylabel("y label")
plt.xlabel("x label")

plt.legend()

plt.show()
