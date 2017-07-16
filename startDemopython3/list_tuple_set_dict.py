#!/sys/bin/python3

#List  note :list have many built-in functions
list = [2,3,"zh",3.4,5+7j]
print (list)
print (list[2])
print (list[2:4])
print (list*2)
list[1]="3str"
print (list[-1])


#tuple
tuple=( 1,2,3,4,5 )

print (tuple) 

print (tuple[2])

print (tuple[2:4])

print (tuple[:-1])

print (tuple[-1])

#set

set = {"123","234","345","890","322"}

print (set)

if("123" in set):
	print ("123 is in set")
else:
	print ("123 is not in set");



set1 = {"123","234","345","890","300"}

print (set1 - set)


print (set | set1)

print (set1 & set)

print (set1 ^ set)

#dictionary

dict = {}

dict["one"]="one"

dict["two"]="two"

dict["three"]="three"

tinydict={"four":"four","five":"five","six":"six","seven":"seven"}

print (dict)

print (tinydict)

print (tinydict.keys())

print (dict.keys())

print (dict.values())

