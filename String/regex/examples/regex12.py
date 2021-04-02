# finding n in words
import re
searchstring='Vishnu Narayan Krishna Bholenath Ram Hanuman Laxman Bharat '
print(re.findall(r'[a-zA-Z]+n[a-zA-Z]',searchstring))
