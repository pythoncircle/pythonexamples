import re


p = re.compile('(a(b)c)d')
m = p.match('abcd')

if m:
	print(m.group())
	print(m.group(0))
	print(m.group(1))
	print(m.group(2))
else:
	print('did not match')


"""
print(m.group(1))
print(m.group(2))
print(m.group(2,1,2))
print(m.groups())
"""
