import random

def adivina_mi_numero():
	
	nro_secreto=random.randint(1, 20)
	intentos=5

	print('Bienvenido al juego Adivina mi numero!')
	print('')
	print('Tienes 5 intentos para adivinar el numero secreto (Entre 1 y 20).')
	print('')

	while intentos>0:

		print('Intento:', 6 - intentos)
		print('')
		nro=int(input('Ingresa tu numero: '))
		print('')
		
		if nro==nro_secreto:
			
			print('Adivinaste, mi numero era', nro_secreto)
			return
			
		elif nro<nro_secreto:
			
			print('Mi numero es mayor.')
			print('')
			
		else:
			
			print('Mi numero es menor.')
			print('')

		intentos-=1

	print('No adivinaste, mi numero era', nro_secreto)

adivina_mi_numero()
      