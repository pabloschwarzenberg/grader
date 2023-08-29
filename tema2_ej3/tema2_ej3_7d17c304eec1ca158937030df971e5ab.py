def numero_perfecto(a):
	
	sd=0
	
	for i in range(1, a):
		
		if a % i == 0:
			sd+=i
			
	return sd==a

if __name__ == '__main__':
	
	numero=int(input('Ingrese un numero: '))
	print('')
	
	if numero_perfecto(numero):
		
		print(str(numero)+' es un numero perfecto.')
		
	else:
		
		print(str(numero)+' no es un numero perfecto.')