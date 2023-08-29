#Suma de los N primeros números

N=int(input('Ingrese un numero natural hasta el cual sumar: '))

if N>=1:
	n=(N*(N+1))/2

	print('')
	print('Suma de los numeros naturales del 1 hasta el '+str(N)+': '+str(int(n)))
	print('')

else:
	print('')
	print('INGRESE UN NUMERO NATURAL')
	print('')