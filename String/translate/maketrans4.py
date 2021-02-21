str='mathematics'
a="ema"  # characters to be replaced
b="zno"  # replacement characters
c="tcs"   # characters to be removed

transtable=str.maketrans(a,b,c)

print(str.translate(transtable))