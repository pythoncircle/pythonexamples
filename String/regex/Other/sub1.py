import re

pattern = 'a...s'
test_string = 'mangoabyss'
result = re.search(pattern, test_string)

if result:
  print("just found")
else:
  print("never found")	
