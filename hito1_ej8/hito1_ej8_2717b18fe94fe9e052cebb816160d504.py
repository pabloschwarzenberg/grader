#Descomponer un número
      
n = input("Ingrese un número de 4 dígitos: ")
nlist = list(n)

while not(len(nlist) == 4):
	nlist.insert(0, 0)

if(nlist[0] == 0):
	if(nlist[1] == 0):
		if(nlist[2] == 0):
			if(nlist[3] == 0):
				print("0")
			else:
				print(nlist[3], 'U')
		else:
			print(nlist[2], 'D +', nlist[3], 'U')
	else:
		print(nlist[1], 'C +', nlist[2], 'D +', nlist[3], 'U')
else:
	print(nlist[0], 'M +', nlist[1], 'C +', nlist[2], 'D +', nlist[3], 'U')