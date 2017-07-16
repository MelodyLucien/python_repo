#!/usr/bin/python3
import sys

print(sys.argv)

print(sys.argv[1])

sys.stderr.write("i am stderr!\n")

sys.stderr.flush()


sys.stdout.write("i am stdout\n")




