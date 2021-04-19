import re


p = re.compile('abcd')
m = p.match('abcd')

if m:
	print(m.group(0))
else:
	print('did not match')


