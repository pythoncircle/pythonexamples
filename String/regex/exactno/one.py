import re

pattern=re.compile(r'a{2}')

matchedResult=pattern.findall('apple')

if matchedResult:
	print('matched',mathcedResult)
else:
	print('not matched')	
