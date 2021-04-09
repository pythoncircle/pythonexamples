import re

pattern=re.compile(r'\bkrishna\b')

matchedResult=pattern.finditer('mathura krishna radheykrishna krishnakrishna barsana krishnameera vrindavan ')

for match in matchedResult:
	print('matched',match.group(),match.span())
