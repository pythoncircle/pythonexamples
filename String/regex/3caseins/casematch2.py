import re

pattern=re.compile('krishna',re.IGNORECASE)
matchedResult=pattern.match('Krishna')

if matchedResult:
	print('matched')
else:
	print('not matched')
 