num=80

def one():
    num=50
    print("num inside one ",num)

    def two():
        num=20	
        print("num inside two ",num)

    two()

one()

print("num outside ",num)
 
  
    

