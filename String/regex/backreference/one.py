import re
p=re.compile(r'\b(\w+)\s+\1\b')
match=p.search('Paris in the the spring')
if match:
	print(match.group())
else:
	print('not matched')