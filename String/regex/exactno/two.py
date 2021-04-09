import re

pattern=re.compile(r'a{2}')

matchedResult=pattern.findall('apaaplaaae')

if matchedResult:
	print('matched',matchedResult)
else:
	print('not matched')	
