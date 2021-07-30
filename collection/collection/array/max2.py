import array

arr=array.array("i",[4,38,52,74,32])

big=arr[0]

for k in arr:
	
    if k>big:
      big=k

print(big)