import re

p=re.compile(r'\b(\w+)\s+\1\b')

result=p.findall('Paris in the the spring')

print(result)

"""
findall just returns the captured groups

https://stackoverflow.com/questions/6018340/capturing-group-with-findall
"""