a, b = 10, 20
  
# Use tuple for selecting an item 
# (if_test_false,if_test_true)[test] 
print( (b, a) [a < b] ) 


"""  
Use Dictionary for selecting an item 
print({True: a, False: b} [a < b]) 
lamda is more efficient than above two methods 
because in lambda  we are assure that 
only one expression will be evaluated unlike in 
tuple and Dictionary 

print((lambda: b, lambda: a)[a < b]()) 
"""