import re

msg ="""<p>
  This is a paragraph.
  It has multiple lines.
  </p>
"""

pattern=re.compile(r'^It has.*',re.MULTILINE)
matchedResult=pattern.search(msg)

if matchedResult:
	print(matchedResult.group())
else:
	print('no not matched')
 