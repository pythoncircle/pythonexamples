import re

pattern=re.compile(r'a')

matchedIter=pattern.finditer('abdacthayakpa')

for match in matchedIter:
	print(match.group(),match.span())
