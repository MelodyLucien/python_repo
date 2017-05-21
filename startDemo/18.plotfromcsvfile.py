#!/usr/bin/python3

# pip3 install matplotlib
from matplotlib import pyplot as plt
import numpy as np

x,y=np.loadtxt('exm2.csv',unpack=True,delimiter=',')


plt.scatter(x,y,color='r',linewidth=10,label='today')


#add labels
plt.grid(True,color='k')
plt.title("My Chart")
plt.ylabel("y label")
plt.xlabel("x label")

plt.legend()

plt.show()

