#Contestador de celular
whitelist=['9', '0', '9']
blacklist=['8', '7', '7']

n=input("Ingrese número telefónico: ")
h=int(input("Ingrese hora de llamada: "))

nlist=list(n)
nver1=nlist[5:]
nver2=nlist[:2]

s='CONTESTAR'

if(0 <= h <= 7):
	print(s)
elif(8 <= h < 14 ):
	if(nver1.sort() == whitelist.sort()):
		print(s)
	else:
		print('NO ' + s)
elif(17<= h <=  19):
	if(nver2.sort() == blacklist.sort()):
		print('NO ' + s)
	else:
		print(s)
else:
	print('NO ' + s)