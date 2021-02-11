# indirect recursion

def one():
    print("Heyyyy  this is one")
    two()

def two():
    print("Hiii  this is two")
    one()


one()




