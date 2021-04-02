import re

pattern=re.compile('^5+')
matchedResult=pattern.findall('51234')

if matchedResult:
	print('matched ',matchedResult)
else:
	print('not matched')
 