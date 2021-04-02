import re

result = re.sub('abc(def)ghi', r'\1', input)    # Replace a string with a part of itself
print(result)