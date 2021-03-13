import re as delhi

match=delhi.search('ba[artz]', 'foobarqux')

print(match.group()) # group is returning the substring in which the pattern exists
