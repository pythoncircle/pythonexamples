def one():
	yield 1
	yield 2
	yield 3
	yield 4
	yield 5

for k in one():
	print(k)
