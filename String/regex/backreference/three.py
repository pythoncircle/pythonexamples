import re

p=re.compile(r'\b(\w+)\s+\1\b')

result=p.findall('Paris Paris in the the spring')

print(result)

