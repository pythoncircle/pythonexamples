import re

pattern=re.compile(r'krishna\Z')

matchedResult=pattern.finditer('mathura krishna radheykrishna krishnakrishna barsana krishnameera vrindavan krishna')

for match in matchedResult:
	print('matched',match.group(),match.span())
