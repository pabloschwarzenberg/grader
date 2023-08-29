def SubsecuenciaADN(secuencia, n):

	frecuencia={}

	for i in range(len(secuencia)-n+1):
		
		subsecuencia=secuencia[i:i+n]
		
		if subsecuencia in frecuencia:
			
			frecuencia[subsecuencia]+=1
			
		else:
			
			frecuencia[subsecuencia]=1

	subsecuencias=[subsecuencia for subsecuencia, count in frecuencia.items() if count==1]

	return subsecuencias

adn=input("Ingrese la secuencia: ")
n=int(input("Ingrese el valor de n: "))

subsecuencias=SubsecuenciaADN(adn, n)

if subsecuencias:
	
	for subsecuencia in subsecuencias:
		
		print(subsecuencia)
		
else:
	
	print("ninguna")