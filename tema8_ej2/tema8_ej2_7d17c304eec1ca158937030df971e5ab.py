def buscarTodas(a, b):
	
	letras=[]
	lectura=0
	
	while (1):
		
		letra=a.find(b, lectura)
		
		if letra==-1:
			
			break
			
		letras.append(str(letra))
		
		lectura=letra+1
		
	return ' '.join(letras)

if __name__=='__main__':
	
	a=input('Ingrese el string a: ')
	b=input('Ingrese el string b: ')
	
	P = buscarTodas(a, b)
	
	print('')
	print('El resultado es:', P)     