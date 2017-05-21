#!/usr/bin/python3

'''
Identifiers:

\d
\D
\s
\S
\w
\W
.
\b
\.

Modifiers:
{1,3}
+
?  zero or 1
*   
$ the end of string
^ the begining of a string
| ether or 
[] range or variance
{x}

White space characters:
\n
\s
\t

\e
\f
\r

DONT FORGET!:

. + * ? [] $ ^ () {} | \

'''

import re

exampleStr='''
 Bob is 12 years old,and her grandpa is 69 years old.
 Kiilly is 20 years old,and his mother ,Oscar ,is 120. 
'''

ages=re.findall(r'\d{1,3}',exampleStr)
names=re.findall(r'[A-Z][a-z]*',exampleStr)

print(ages)
print(names)




