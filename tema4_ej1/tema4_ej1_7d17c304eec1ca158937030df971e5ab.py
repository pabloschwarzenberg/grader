import random

def ocultar_letras(palabra, cantidad):
	
	LetrasOc=random.sample(range(len(palabra)), cantidad)
	PalabraOc=list(palabra)
	
	for i in LetrasOc:
		PalabraOc[i]='_'
		
	return ''.join(PalabraOc)

def revisar_letra(PalabraSec, palabra, letra):
	
	nueva_palabra=list(palabra)
	
	for i in range(len(PalabraSec)):
		if PalabraSec[i]==letra:
			nueva_palabra[i]=letra
			
	return ''.join(nueva_palabra)

if __name__=='__main__':
	
	PalabraRandom=['submarino', 'auto', 'venta', 'tigre', 'leona', 'centrifugados']
	PalabraSec=random.choice(PalabraRandom)
	letras_mostradas=random.randint(1, len(PalabraSec))
	PalabraLuz=ocultar_letras(PalabraSec, letras_mostradas)
	intentos=7

	print('ADIVINA LA PALABRA SECRETA')
	print('')
	print('La palabra tiene '+str(len(PalabraSec))+' letras.')
	print('')
	print('La palabra mostrada es: ', PalabraLuz)
	print('')

	while intentos > 0:
		
		letra=input('Ingresa una letra o la palabra completa: ')

		if len(letra)==1:
			
			PalabraLuz = revisar_letra(PalabraSec, PalabraLuz, letra)
			print('')
			print('La palabra mostrada es: ', PalabraLuz)

			if PalabraLuz==PalabraSec:
				
				print('')
				print('Has adivinado la palabra secreta!')
				break
				
			else:
				
				intentos-=1
				print('')
				print('Letras restantes: '+str(intentos))
				print('')
				
		elif len(letra)>1 and letra==PalabraSec:
			
			print('')
			print('Has adivinado la palabra secreta!')
			break
			
		else:
			
			print('')
			print('La letra o palabra ingresada es incorrecta.')
			print('')

		if intentos==0:
			
			print('')
			print('Has agotado tus intentos. La palabra secreta era: ', PalabraSec)         