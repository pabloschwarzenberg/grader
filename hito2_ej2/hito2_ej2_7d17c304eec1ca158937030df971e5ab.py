def validar_secuencia(adn):
	
	adn=adn.lower()

	for nucleotido in adn:
		
		if nucleotido!='a' and nucleotido!='c' and nucleotido!='t' and nucleotido!='g':
			
			return False

	return True

adn_input=input("Ingrese la adn de ADN: ")

if validar_secuencia(adn_input):
	
	print("Secuencia correcta")

else:

	print("Secuencia incorrecta")