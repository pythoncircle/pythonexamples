import re

pattern=re.compile('\S+')
matchedResult=pattern.findall('computer science      python')

if matchedResult:
	print(' matched certainly',matchedResult)
else:
	print('oops not matched')
 