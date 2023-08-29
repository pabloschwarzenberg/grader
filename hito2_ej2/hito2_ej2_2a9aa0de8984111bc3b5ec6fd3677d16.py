def ValidarADN(secuencia):
	
	secuencia=secuencia.lower()

	for nucleotido in secuencia:
		
		if nucleotido!='a' and nucleotido!='c' and nucleotido!='t' and nucleotido!='g':
			
			return False

	return True

secuencia_input=input("Ingrese la secuencia de ADN: ")

if ValidarADN(secuencia_input):
	
	print("Secuencia correcta")

else:

	print("Secuencia incorrecta")