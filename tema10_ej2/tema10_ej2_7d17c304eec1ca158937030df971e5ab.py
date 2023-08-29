#La función debe retornar la distancia como un string
# +1 : si la distancia es mayor que 1
# IB : si la distancia es 1, y para llegar de una palabra a la otra hay que
#      insertar o borrar una letra
# 1S : si la distancia es 1 porque hay que sustituir una letra
# 0D : si las palabras son iguales
def levenshtein(P1, P2):
	
	if P1==P2:
		
		return '0D'

	x=len(P1)
	y=len(P2)

	if abs(x-y)>1:
		
		return '+1'
		
	if x>y:
		
		P1, P2 = P2, P1
		x, y = y, x

	Matriz=[[0] * (y + 1) for _ in range(x + 1)]

	for i in range(x + 1):
		
		Matriz[i][0] = i

	for j in range(y + 1):
		
		Matriz[0][j] = j

	for i in range(1, x + 1):
		
		for j in range(1, y + 1):
			
			if P1[i - 1] == P2[j - 1]:
				
				Matriz[i][j] = Matriz[i - 1][j - 1]
				
			else:
				
				Matriz[i][j] = min(Matriz[i - 1][j] + 1,Matriz[i][j - 1] + 1,Matriz[i - 1][j - 1] + 1)

	Dis = Matriz[x][y]

	if Dis>1:
		
		return '+1'
		
	elif Dis==1:
		
		return 'IB' if x<y else '1S'
		
	else:
		
		return '0D'

if __name__=='__main__':
	
	P1=input('Ingrese la primera palabra: ')
	P2=input('Ingrese la segunda palabra: ')
	
	Efecto=levenshtein(P1, P2)
	
	print('')
	
	print(Efecto)       