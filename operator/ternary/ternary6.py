a, b = 32000, 9000
  
"""
lamda is more efficient than above two methods 
because in lambda  we are assure that 
only one expression will be evaluated unlike in 
tuple and Dictionary 
"""

print((lambda: b, lambda: a)[a < b]()) 
