import re

pattern=re.compile('\d{10,10}')
matchedResult=pattern.findall('1234567898')

if matchedResult:
	print('yes matched ',matchedResult)
else:
	print('no not matched')
 