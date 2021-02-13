# closure

# outer function or enclosing function
def one(a):
    # inner function
    def two(b):
        print(a*b)
    return two

abc=one(5)

abc(3)

del one

abc(7)
