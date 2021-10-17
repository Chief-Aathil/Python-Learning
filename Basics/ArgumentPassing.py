#invoke the python interpreter with any string as command line arguments to print the same
# ex: 
#>>> python ArgumentPassing.py Hello
# In this example the first argument is the fileanme itself and the second is the string 'Hello'

import sys
print (sys.argv[0])
print(sys.argv[1])