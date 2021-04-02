import re

# ^ outside square bracket means character after ^ must be present at the beginning

pattern=re.compile('^5+') 
  
matchedResult=pattern.findall('1234')

if matchedResult:
	print('matched ',matchedResult)
else:
	print('not matched')
 