str='mathematics'
a="cma"  # characters to be replaced
b="zno"  # replacement characters

transtable=str.maketrans(a,b)

print(str.translate(transtable))