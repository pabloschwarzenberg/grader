def rot13(palabra):
	
	PalabraEncriptada=''
	
	for letra in palabra:
		
		if letra.isalpha():
			
			if letra.isupper():
				
				LetraEncriptada = chr((ord(letra) - 65 + 13) % 26 + 65)
			else:
				
				LetraEncriptada = chr((ord(letra) - 97 + 13) % 26 + 97)
				PalabraEncriptada += LetraEncriptada
		else:
			
			PalabraEncriptada += letra
			
	return PalabraEncriptada

if __name__=='__main__':
	
	palabra=input('Ingresa una que quieras encriptar: ')
	palabra=palabra.lower()
	obj=Rot13(palabra)
	print('')
	print('El obj es:', obj)        