import re

emailId='pythoncircle@gmail#com'
pattern=re.compile('[a-zA-Z0-9_]+@gmail\.com') # we escaped the normal meaning of .
matchedResult=pattern.match(emailId)

if matchedResult:
	print('matched')
else:
	print('did not match')

