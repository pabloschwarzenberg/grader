#Descomponer un número
nro=input()
nro=[nro[i] for i in reversed(range(len(nro)))]
lista=[nro[i] + ((i+1==1 and 'U') or (i+1==2 and 'D+') or (i+1==3 and 'C+') or (i+1==4 and 'M+')) for i in range(len(nro))]
for i in reversed(range(len(nro))):
	print(lista[i],end='')
