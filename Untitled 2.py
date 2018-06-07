import hashlib
s = open("file1.txt","rb")
b = s.read()
m = hashlib.sha384()
m.update (b)
print (m.hexdigest())
#print hashed value

import hashlib
s = open("file2.txt","rb")
b = s.read()
m = hashlib.sha384()
m.update (b)
print (m.hexdigest())
#print hashed value


import hashlib
s = open("file3.txt","rb")
b = s.read()
m = hashlib.sha384()
m.update (b)
print (m.hexdigest())
#print hashed value

