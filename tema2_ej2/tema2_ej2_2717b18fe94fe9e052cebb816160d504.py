# completa el código de la función

def amigos(a, b):
	if(a == b):
		state=False
	else:
		lista=[]
		listb=[]
		state=False
		for i in range(2, a+1):
			x = a % i 
			if(x == 0):
				lista.append(i)
		for j in range(2, b+1):
			y = b % j 
			if(y == 0):
				listb.append(j)
		suma=sum(lista)
		sumb=sum(listb)
		if(suma == sumb):
			state=True
	return state