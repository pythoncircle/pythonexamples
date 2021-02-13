
def one(num):    
    def two():
        nonlocal num 
        num=num+1
        return num
    return two


z=one(8)

print(z())
print(z())
print(z())
print(z())



