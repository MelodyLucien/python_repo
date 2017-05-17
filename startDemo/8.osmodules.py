#!/usr/bin/python3
import os

curDir=os.getcwd()

print(curDir)

os.mkdir("tmp.file")

import time

time.sleep(2)

os.rename("tmp.file","renamefile")

time.sleep(2)

os.rmdir("renamefile")


print("over")


