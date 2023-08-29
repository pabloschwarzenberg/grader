#Sistema de Ecuaciones
def sistema(n1, n2, n3, n4, n5, n6):
	
	denominador= n1 * n5 - n4 * n2

	if denominador==0:
		
		return False

	x=(n3 * n5 - n6 * n2)/denominador
	y=(n1 * n6 - n4 * n3)/denominador

	return x , y


n1=float(input('Ingrese el coeficiente de x en la primera ecuacion: '))
print('')
n2=float(input('Ingrese el coeficiente de y en la primera ecuacion: '))
print('')
n3=float(input('Ingrese el termino independiente de la primera ecuacion: '))
print('')
n4=float(input('Ingrese el coeficiente de x en la segunda ecuacion: '))
print('')
n5=float(input('Ingrese el coeficiente de y en la segunda ecuacion: '))
print('')
n6=float(input('Ingrese el termino independiente de la segunda ecuacion: '))
print('')


soluciones=sistema(n1, n2, n3, n4, n5, n6)


if soluciones is False:
	
	print('El sistema de ecuaciones no tiene solucion unica.')

else:

	solx=round(soluciones[0], 1)
	soly=round(soluciones[1], 1)
	print('Soluciones del sistema son:')
	print('')
	print('x=',solx)
	print('y=',soly)      