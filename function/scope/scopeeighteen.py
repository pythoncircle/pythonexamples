num=80

def two():
    nonlocal num
    num=20	
    print("num inside two ",num)

two()
print("num outside two ",num)

# nonlocal scope is available only inside the nested/inner function.

