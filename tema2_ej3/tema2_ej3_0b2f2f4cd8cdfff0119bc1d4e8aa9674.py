def numero_perfecto(a):
	
	sumadivisores=0
	
	for i in range(1, a):
		
		if a % i == 0:
			sumadivisores+=i
			
	return sumadivisores==a

if __name__ == '__main__':
	
	nro=int(input('Ingrese un numero: '))
	print('')
	
	if numero_perfecto(nro):
		
		print(str(nro)+' es un numero perfecto.')
		
	else:
		
		print(str(nro)+' no es un numero perfecto.')