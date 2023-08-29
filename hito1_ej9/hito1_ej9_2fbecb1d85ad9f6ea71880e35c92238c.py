def sis(a1, b1, c1, a2, b2, c2):
	
	denominador= a1 * b2 - a2 * b1

	if denominador==0:
		
		return False

	x=(c1 * b2 - c2 * b1)/denominador
	y=(a1 * c2 - a2 * c1)/denominador

	return x , y


a1=float(input('Ingrese el coeficiente de x en la primera ecuacion: '))
print('')
b1=float(input('Ingrese el coeficiente de y en la primera ecuacion: '))
print('')
c1=float(input('Ingrese el termino independiente de la primera ecuacion: '))
print('')
a2=float(input('Ingrese el coeficiente de x en la segunda ecuacion: '))
print('')
b2=float(input('Ingrese el coeficiente de y en la segunda ecuacion: '))
print('')
c2=float(input('Ingrese el termino independiente de la segunda ecuacion: '))
print('')


soluciones=sis(a1, b1, c1, a2, b2, c2)


if soluciones is False:
	
	print('El sistema de ecuaciones no tiene solucion unica.')

else:

	solx=round(soluciones[0], 1)
	soly=round(soluciones[1], 1)
	print('Las soluciones del sistema son:')
	print('')
	print('x=',solx)
	print('y=',soly)
