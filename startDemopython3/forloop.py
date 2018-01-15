#!/usr/bin/python3


'''
for

'''

exampleList = [1,2,314,413,6,8,9,10,20]
for i in exampleList:
	print(i)
	print("continue")

print(exampleList)

length = len(exampleList)

for i in range(0,length):
	exampleList[i] = exampleList[i] + 1

print(exampleList)


emptyList = []

emptyList.append(1) 
emptyList.append(12)

print("emptyList:",emptyList)



# out of for loop
print("over")
 
# range built-in function
for x in range(1,11):
	print(x)

