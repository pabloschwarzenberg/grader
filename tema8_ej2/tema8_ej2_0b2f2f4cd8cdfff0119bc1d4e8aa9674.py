def buscarTodas(a, b):
	
	letras=[]
	lectura=0
	
	while True:
		
		letra=a.find(b, lectura)
		
		if letra==-1:
			
			break
			
		letras.append(str(letra))
		
		lectura=letra+1
		
	return ' '.join(letras)

if __name__=='__main__':
	
	a=input('Ingresa el string a: ')
	b=input('Ingresa el string b: ')
	
	posiciones = buscarTodas(a, b)
	
	print('')
	print('El resultado es:', posiciones)
           