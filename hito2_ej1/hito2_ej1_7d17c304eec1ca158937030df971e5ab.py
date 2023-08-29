def AlineacionDeADN(x, y):

	w=""
	z=0

	for i in range(len(x)):
		
		if z<len(y) and x[i]==y[z]:
			
			w+=y[z]
			z+=1
			
		else:
			
			w+="_"


	if z<len(y):
		
		w+=y[z:]

	return w


Adn1=input("Ingrese la primera secuencia: ")
Adn2=input("Ingrese la segunda secuencia: ")


ADNalineado=AlineacionDeADN(Adn1, Adn2)


print(ADNalineado)      