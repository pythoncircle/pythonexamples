import re

pattern=re.compile('[0-9]{10,10}')
matchedResult=pattern.findall('1234567898')

if matchedResult:
	print('matched ',matchedResult)
else:
	print('not matched')
 