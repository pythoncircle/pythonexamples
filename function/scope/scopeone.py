# scope 
a=10 # global scope

def display():
    a=20 # local scope
    print("a inside display",a)

display()

print("a outside display",a)

""" variable declared outside a method has global scope where as variable declared inside a method has local scope """