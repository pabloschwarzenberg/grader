import random

def Adivina():
	
	n=random.randint(1, 20)
	intentos=5

	print('Bienvenido al juego Adivina mi numero!')
	print('')
	print('Tienes 5 intentos para adivinar el numero secreto (Entre 1 y 20).')
	print('')

	while intentos>0:

		print('Intento:', 6 - intentos)
		print('')
		numero=int(input('Ingresa tu numero: '))
		print('')
		
		if numero==n:
			
			print('Adivinaste, mi numero era', n)
			return
			
		elif numero<n:
			
			print('Mi numero es mayor.')
			print('')
			
		else:
			
			print('Mi numero es menor.')
			print('')

		intentos-=1

	print('No adivinaste, mi numero era', n)

Adivina()      