num=80

def one():
    num=50
    print("num inside one ",num)

    def two():
        nonlocal num
        num=20	
        print("num inside two ",num)

    two()
    print("num outside two ",num)

one()

print("num outside ",num)

# one is the enclosing method of two 
  
"""
there are three scopes of variables :
1 global
2 local
3 nonlocal
"""



    

