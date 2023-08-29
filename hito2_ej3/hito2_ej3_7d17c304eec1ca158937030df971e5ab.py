def SubsecuenciaADN(y, n):

	frecuencia={}

	for i in range(len(y)-n+1):
		
		h=y[i:i+n]
		
		if h in frecuencia:
			
			frecuencia[h]+=1
			
		else:
			
			frecuencia[h]=1

	k=[h for h, count in frecuencia.items() if count==1]

	return k

adn=input("Ingrese el valor de y: ")
n=int(input("Ingrese el valor de n: "))

k=SubsecuenciaADN(adn, n)

if k:
	
	for h in k:
		
		print(h)
		
else:
	
	print("ninguna")    