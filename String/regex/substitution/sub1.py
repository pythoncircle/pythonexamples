import re


txt='mango apple pineapple jackfruit pomegranate apple banana orange'
matchedResult=re.sub('apple','kiwi',txt)

if matchedResult:
	print('matched',matchedResult)
else:
	print('did not match')

