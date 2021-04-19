import re


p = re.compile('(a(b)c)d')
m = p.match('abcd')

if m:
	print(m.group(2,1,2))
else:
	print('did not match')


