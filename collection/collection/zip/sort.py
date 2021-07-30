letters = ['b', 'a', 'd', 'c']
numbers = [2, 4, 3, 1]

data1 = list(zip(letters, numbers))
data1.sort()  # Sort by letters

data2 = list(zip(numbers, letters))
data2.sort()  # Sort by numbers

print(data1)
print(data2)
