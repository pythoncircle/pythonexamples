import re

name='Laxmi Narayan Vishnu Krishna'

match=re.search('n',name) # n is pattern , name is the search string in which the pattern 
# would be searched

if match:
  print(match.span())
else:
  print('not found')

