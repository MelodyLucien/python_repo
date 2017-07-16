#!/usr/bin/python3
import csv

pics=[]

nums=[]

with open('emp.csv') as csvfile:
	readCsv = csv.reader(csvfile,delimiter=',')

	for row in readCsv:
		print(row)
		picture=row[0]
		number=row[2]
		pics.append(picture)
		nums.append(number)

print(pics)
print(nums)


number=input("which pic do you want to look at?")

print("info is :")
print("pic name:",pics[int(number)])
print("pic num: ",nums[int(number)])

