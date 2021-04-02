import re

pattern=re.compile('krishna')
matchedResult=pattern.match('Krishna')

if matchedResult:
	print('matched')
else:
	print('not matched')
 