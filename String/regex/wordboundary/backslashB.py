import re

pattern=re.compile(r'\Bkrishna\B') # krishna should neither be at the beginning nor at the end of a word

matchedResult=pattern.finditer('mathura krishna radheykrishna gopalkrishnagokulwale krishnakrishna barsana krishnameera vrindavan ')

for match in matchedResult:
	print('matched',match.group(),match.span())
