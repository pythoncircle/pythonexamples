import re


txt='mango apple pineapple jackfruit pomegranate apple banana orange'
matchedResult=re.subn('apple','kiwi',txt)

if matchedResult:
	print('matched',matchedResult)
	print('matchedResult[0]=',matchedResult[0])
	print('matchedResult[1]=',matchedResult[1])
else:
	print('did not match')

