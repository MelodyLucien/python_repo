#!/usr/bin/python3


'''
readline() readlines(),read()

'''

savefile = open("tt.txt","r")

# r
readline=savefile.readlines()

readStr = savefile.read()

savefile.close()

print(readStr)

print("\n")

print(readline)


















