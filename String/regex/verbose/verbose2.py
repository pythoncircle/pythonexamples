import re

pattern=re.compile(r"""
 apple | orange 
""",re.VERBOSE
)

matchedResult=pattern.finditer('apple mango pineapple jackfruit orange pomegranate apple banana orange')

for match in matchedResult:
	print('matched',match.group(),match.span())
