import re

name='Laxmi Narayan Vishnu Krishna'

match=re.search('n',name)

if match:
  print(match.group())
else:
  print('not found')

