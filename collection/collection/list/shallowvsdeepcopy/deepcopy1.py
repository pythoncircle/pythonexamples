import copy

list1=[[10],[20],[30]]
list2=copy.deepcopy(list1)
list2[0][0]=500

print(list1)
print(list2)

# https://pythoncircle.blogspot.com/2021/08/shallow-copy-vs-deep-copy.html



