import re

m = re.match("(?:[abc])+", "abc")
print(m.groups())


