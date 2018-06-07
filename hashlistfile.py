import hashlib
import os

items= os.listdir (".")

for n in items:
	f = open(n,'rb')
	f2 = f.read()
	m = hashlib.sha256()
	m.update(f2)
	print (m.hexdigest())	
	#hash fileslist
		

