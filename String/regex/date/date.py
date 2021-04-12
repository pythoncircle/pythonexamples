import re

pattern=re.compile(r'(?:(?:([12][0-9])|(?:3[01]))|(?:[^1-9][1-9]))/\d{1,2}/\d{1,4}')

matchedResult=pattern.finditer('Once 12/8/2000 then on 15/3/2021 she 52/78/1935 abc 27/02/2021 on 5/1/2021 ')


for match in matchedResult:
	print(match.group())
