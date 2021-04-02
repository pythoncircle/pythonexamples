import re

pattern=re.compile('[a-z]+:\\\[a-z]+')
matchedResult=pattern.match('d:\python')

if matchedResult:
	print('matched')
else:
	print('not matched')
 