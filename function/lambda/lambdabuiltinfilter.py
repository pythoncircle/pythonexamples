
"""
filter function returns a list
filter function accepts function and list as arguements
"""

def one(x):
	if x%2==0:
		return True
	else:
		return False


list1=[100,120,15,52,80,13,17]

list2=list(filter(lambda x: x%2==0,list1))

list2=list(filter(one,list1))

print('list1 is ',list1)
print('list2 is ',list2)