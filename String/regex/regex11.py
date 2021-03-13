import re as delhi

match=delhi.search('ba[artz]', 'foobaqux')

if match:
  print(match.group()) # group is returning the substring in which the pattern exists
else:
  print(match)
