import random

def ocultar_letras(palabra, cantidad):
	
	letras_ocultas=random.sample(range(len(palabra)), cantidad)
	palabra_oculta=list(palabra)
	
	for i in letras_ocultas:
		palabra_oculta[i]='_'
		
	return ''.join(palabra_oculta)

def revisar_letra(palabra_secreta, palabra, letra):
	
	nueva_palabra=list(palabra)
	
	for i in range(len(palabra_secreta)):
		if palabra_secreta[i]==letra:
			nueva_palabra[i]=letra
			
	return ''.join(nueva_palabra)

if __name__=='__main__':
	
	palabras_secretas=['submarino', 'auto', 'venta', 'tigre', 'leona', 'centrifugados']
	palabra_secreta=random.choice(palabras_secretas)
	letras_mostradas=random.randint(1, len(palabra_secreta))
	palabra_mostrada=ocultar_letras(palabra_secreta, letras_mostradas)
	intentos=7

	print('ADIVINA LA PALABRA SECRETA')
	print('')
	print('La palabra tiene '+str(len(palabra_secreta))+' letras.')
	print('')
	print('La palabra mostrada es: ', palabra_mostrada)
	print('')

	while intentos > 0:
		
		letra=input('Ingresa una letra o arriesgate con la palabra completa: ')

		if len(letra)==1:
			
			palabra_mostrada = revisar_letra(palabra_secreta, palabra_mostrada, letra)
			print('')
			print('La palabra mostrada es: ', palabra_mostrada)

			if palabra_mostrada==palabra_secreta:
				
				print('')
				print('Felicitaciones! Has adivinado la palabra secreta!')
				break
				
			else:
				
				intentos-=1
				print('')
				print('Letras restantes: '+str(intentos))
				print('')
				
		elif len(letra)>1 and letra==palabra_secreta:
			
			print('')
			print('Felicitaciones! Has adivinado la palabra secreta!')
			break
			
		else:
			
			print('')
			print('La letra o palabra ingresada es incorrecta.')
			print('')

		if intentos==0:
			
			print('')
			print('Lo siento! Has agotado tus intentos. La palabra secreta era: ', palabra_secreta)
         