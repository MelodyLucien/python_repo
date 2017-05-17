#!/usr/bin/python3
#List  note :list have many built-in functions
def sl(x):
	print(x)

list = [2,3,8,3,5+7j]
ll = ["Bob","Alice","Kili","Job"]
print (list)
print (list[2])
print (list[2:4])
print (list*2)

list[1]="3str"

print (list[-1])

list.append("my")

sl(list)

list.insert(0,12)

list.remove(3)

sl(list)

sl(list.index(8))

sl(list.count(3))

ll.sort();

sl(ll)
