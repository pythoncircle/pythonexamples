import re

emailId='pythoncircle@gmail#com'
pattern=re.compile('[a-zA-Z0-9_]+@gmail.com')
matchedResult=pattern.match(emailId)

if matchedResult:
	print('matched')
else:
	print('did not match')

