a, b = 3000, 8000
  
#Use Dictionary for selecting an item 
print({True: 'Radha', False: 'Krishna'} [a < b]) 

"""
lamda is more efficient than above two methods 
because in lambda  we are assure that 
only one expression will be evaluated unlike in 
tuple and Dictionary 

print((lambda: b, lambda: a)[a < b]()) 
"""