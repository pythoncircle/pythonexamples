import re

msg ="""<p>This is Bhoomika paragraph. It has multiple lines.</p>"""


pattern=re.compile(r'<p>.*</p>')
matchedResult=pattern.search(msg)

if matchedResult:
	print(' yes matched ',matchedResult)
else:
	print('no not matched')
 