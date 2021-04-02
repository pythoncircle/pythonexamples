import re

pattern=re.compile(r'[a-z]+:\\[a-z]+')
matchedResult=pattern.match('d:\python')

if matchedResult:
	print('matched matched everywhere')
else:
	print('not matched')
 