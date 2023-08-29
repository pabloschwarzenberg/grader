#Suma de los N primeros números
Numero=int(input('Ingrese un numero natural: '))

if Numero>=1:
	suma=(Numero*(Numero+1))/2

	print('')
	print('Suma de los numeros naturales del 1 hasta el '+str(Numero)+': '+str(int(suma)))
	print('')

else:
	print('')
	print('Numero incorrecto')
	print('')      