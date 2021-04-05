import re


pattern=re.compile(r'\w+')
result=pattern.sub('apple', 'mango orange banana 8 pomegranate')

if result:
	print(result)
else:
	print('no')

"""
msg=re.sub(r'\w+', 'word', 'This phrase contains 5 words')
print(msg)
"""