import array

arr1=array.array("i",[10,20,30,40])
arr2=array.array("i",[100,200,300,400])

arr1.extend(arr2)

print(arr1)
