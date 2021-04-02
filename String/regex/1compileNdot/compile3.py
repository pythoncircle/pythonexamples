import re

emailId='pythoncircle@gmailkcom'
pattern=re.compile('[a-zA-Z0-9_]+@gmail.com')
matchedResult=pattern.match(emailId)

if matchedResult:
	print('match kar gaya')
else:
	print('did not match')

