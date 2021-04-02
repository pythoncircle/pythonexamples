import re

emailId='pythoncircle@'
pattern=re.compile('[a-zA-Z0-9_]+@')
matchedResult=pattern.match(emailId)

if matchedResult:
	print('matched')
else:
	print('did not match')


"""
# greedy character
+ one or more
* 0 or more
"""