import re

pattern=re.compile('[a-z]+:[a-z]+')
matchedResult=pattern.match('d:python')

if matchedResult:
	print('match karega')
else:
	print('not matched')
 