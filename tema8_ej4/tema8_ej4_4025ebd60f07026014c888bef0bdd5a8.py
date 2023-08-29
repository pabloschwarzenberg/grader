from sys import argv 
alph=map(chr, range(97,123)) 
lng=len(alph) 

def rot13(msg): 
	ciph=""
	for lttr in msg: 
		if not lttr.isalpha():
			ciph+=lttr
		elif lttr.islower():
			ciph+=alph[(alph.index(lttr)+13)%lng]
		elif lttr.isupper():
			ciph+=alph[(alph.index(lttr.lower())+13)%lng].upper()
	return ciph

print ("El mensaje cifrado es") 
print (rot13(argv[1]))
print ("El mensaje original es") 
print (rot(rot13(argv[1])))
