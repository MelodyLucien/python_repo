#!/usr/bin/python3

'''

exec just compile and run a command from a str 
so you can just define or run your code

'''
exec("print('so this is a work like eval')")

list_str = "[5,6,7,8,9]"

list_str = exec(list_str)

print(list_str)

exec("list_str2 = [5,6,7,8,9]")
print(list_str2)

exec("def test(): print('o my god ,it works')")
test()


exec("""

def test2():
	print("i can do whatever you want me to do")
""")

test2()
