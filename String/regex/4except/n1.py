import re

pattern=re.compile('[5]+')
matchedResult=pattern.findall('1234')

if matchedResult:
	print('matched ',matchedResult)
else:
	print('not matched')
 