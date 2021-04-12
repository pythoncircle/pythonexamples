import re

"""
Subgroups are numbered from left to right, from 1 upward. Groups can be nested; to determine the number, just count the opening parenthesis characters, going from left to right.
"""

p = re.compile('(a(b)c)d')
m = p.match('abcd')

print(m.group(0))
print(m.group(1))
print(m.group(2))
print(m.group(2,1,2))
print(m.groups())

>>> m = re.match("([abc])+", "abc")
>>> m.groups()
('c',)
>>> m = re.match("(?:[abc])+", "abc")
>>> m.groups()


"""
group() can be passed multiple group numbers at a time, in which case it will return a tuple containing the corresponding values for those groups.
"""

"""
The groups() method returns a tuple containing the strings for all the subgroups, from 1 up to however many there are.
"""

