def hello(num):
    if num==0:
       return 1
    else:
       return num* hello(num-1)    

print(hello(4)) 

