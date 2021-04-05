import re

msg ="""<p>This is Bhoomika paragraph. It has multiple lines.</p>"""


pattern=re.compile(r'<p>.*</p>')
matchedResult=pattern.search(msg)

if matchedResult:
	print(' yes matched ',matchedResult.group())
else:
	print('no not matched')
 