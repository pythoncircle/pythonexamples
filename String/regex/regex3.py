import re

name='Vishnu'

match=re.search('k',name)

if match:
  print(match.group())
else:
  print('not found')

