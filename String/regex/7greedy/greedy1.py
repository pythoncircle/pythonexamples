import re

msg ="<p>This is a paragraph.It has multiple lines.</p>"

pattern=re.compile(r'<.*>')
matchedResultList=pattern.findall(msg)

if matchedResultList:
	print(matchedResultList)
else:
	print('never matched')

 