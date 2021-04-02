import re

name='Laxmi Narayan Vishnu Krishna'

match=re.search('na',name) 

if match:
  print(f'span is {match.span()}')
else:
  print('not found')

