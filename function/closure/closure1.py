# closure

# outer function or enclosing function
def one(a):
    # inner function
    def two(b):
        print(a*b)
    return two


abc=one(5)

abc(3)

# closure is dynamically created function which is returned by other function
In case of closure variable in the scope of enclosing function is retained even after the function call is over
# For closure following three things must be true-
  a) there must be nesting of functions
  b) inner function must refer to the variable in the scope of outer function
  c) outer function must return inner function

