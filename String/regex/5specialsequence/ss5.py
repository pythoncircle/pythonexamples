import re

pattern=re.compile('\s+')
matchedResult=pattern.findall('computer science      python')

if matchedResult:
	print(' matched matched',matchedResult)
else:
	print('never matched')
 