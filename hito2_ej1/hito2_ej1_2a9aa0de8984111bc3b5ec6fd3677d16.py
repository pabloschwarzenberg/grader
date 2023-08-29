def AlinearADN(a, b):

	alineada=""
	z=0

	for i in range(len(a)):
		
		if z<len(b) and a[i]==b[z]:
			
			alineada+=b[z]
			z+=1
			
		else:
			
			alineada+="_"


	if z<len(b):
		
		alineada+=b[z:]

	return alineada


ADN1=input("Ingrese la primera secuencia: ")
ADN2=input("Ingrese la segunda secuencia: ")


ADNalineado=AlinearADN(ADN1, ADN2)


print(ADNalineado)