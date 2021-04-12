import re

pattern=re.compile(r'krishna\Z')

matchedResult=pattern.finditer('mathura krishna radheykrishna krishnakrishna barsana krishnameera vrindavankrishna')

for match in matchedResult:
	print('matched',match.group(),match.span())
