import re

txt='coronaabcdefghivaccine'
result = re.sub('abc(def)ghi', r'\1', txt)    # Replace a string with a part of itself
print(result)