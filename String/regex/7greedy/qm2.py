import re

msg ="abble"

pattern=re.compile(r'b?')
matchedResultList=pattern.findall(msg)

if matchedResultList:
	print(matchedResultList)
else:
	print('never matched')

 