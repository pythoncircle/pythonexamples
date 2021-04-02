import re

replacement = ' '
tobereplaced=r'\s+'
input = '		India     is                  our         motherland     '
result = re.sub(tobereplaced, replacement,   input)    # Eliminate duplicate whitespaces using wildcards

print(result)
