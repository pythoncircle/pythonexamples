import re

pattern=re.compile(r'apple|banana')

matchedResult=pattern.finditer('mango pineapple jackfruit pomegranate banana orange')

for match in matchedResult:
	print('matched',match.group(),match.span())
