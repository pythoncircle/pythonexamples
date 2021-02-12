from functools import reduce
list1 = [2, 3,7, 4, 5, 10] 
total = reduce((lambda a,b: a+b), list1) 
print(total) 