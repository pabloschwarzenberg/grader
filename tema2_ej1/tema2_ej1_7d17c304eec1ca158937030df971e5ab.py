import math

def area_rectangulo(b, a):
	
	return b * a

def area_triangulo(b, a):
	
	return (b * a) / 2

def area_rombo(d1, d2):
	
	return (d1 * d2) / 2

def area_circulo(r):
	
	return math.pi * r**2

if __name__ == '__main__':
	

	print('1. Calcular area de un rectangulo')
	print('2. Calcular area de un triangulo')
	print('3. Calcular area de un rombo')
	print('4. Calcular area de un circulo')
	print('')

	op = int(input('Seleccione una opcion: '))

	if op == 1 :
		
		b = float(input('Ingrese la base del rectangulo: '))
		a = float(input('Ingrese la altura del rectangulo: '))
		area = area_rectangulo(b, a)
		print('')
		print('El area del rectangulo es:', area)
		
	elif op == 2 :
		
		b = float(input('Ingrese la base del triangulo: '))
		a = float(input('Ingrese la altura del triangulo: '))
		area = area_triangulo(b, a)
		print('')
		print('El area del triangulo es:', area)
		
	elif op == 3 :
		
		d1 = float(input('Ingrese la diagonal mayor del rombo: '))
		d2 = float(input('Ingrese la diagonal menor del rombo: '))
		area = area_rombo(d1, d2)
		print('')
		print('El area del rombo es:', area)
		
	elif op == 4 :
		
		r = float(input('Ingrese el radio del circulo: '))
		area = area_circulo(r)
		print('')
		print('El area del circulo es:', area)
		
	else:
		
		print('opcion invalida. Por favor, seleccione una opcion valida.')   