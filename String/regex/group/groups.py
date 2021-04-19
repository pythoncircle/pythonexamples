import re


p = re.compile('(a(b)c)d')
m = p.match('abcd')

if m:
	print(m.groups())
else:
	print('did not match')


