from collections import  defaultdict

dict=defaultdict(lambda : 'its not present')

dict.update({'color':'red',100:'full marks',40:'pass marks'})

print(dict['color'])

print(dict['food'])
