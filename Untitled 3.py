s = open("file1.txt","r")
b = s.read()
if "hello" in b:
	print('word found')
