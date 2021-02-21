str='mathematics'

charmap={'a':'y','m':'n','t':'d'}
transtable=str.maketrans(charmap)

print(str.translate(transtable))