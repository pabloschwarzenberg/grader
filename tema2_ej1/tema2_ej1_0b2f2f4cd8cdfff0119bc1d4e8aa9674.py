import math

def area_rectangulo(base, altura):
	
	return base * altura

def area_triangulo(base, altura):
	
	return (base * altura) / 2

def area_rombo(diagonal1, diagonal2):
	
	return (diagonal1 * diagonal2) / 2

def area_circulo(radio):
	
	return math.pi * radio**2

if __name__ == '__main__':
	
	print('################## MENU ##################')
	print('')
	print('1. Calcular area de un rectangulo')
	print('2. Calcular area de un triangulo')
	print('3. Calcular area de un rombo')
	print('4. Calcular area de un circulo')
	print('')

	opcion = int(input('Seleccione una opcion: '))
	print('')

	if opcion == 1:
		
		base = float(input('Ingrese la base del rectangulo: '))
		altura = float(input('Ingrese la altura del rectangulo: '))
		area = area_rectangulo(base, altura)
		print('')
		print('El area del rectangulo es:', area)
		
	elif opcion == 2:
		
		base = float(input('Ingrese la base del triangulo: '))
		altura = float(input('Ingrese la altura del triangulo: '))
		area = area_triangulo(base, altura)
		print('')
		print('El area del triangulo es:', area)
		
	elif opcion == 3:
		
		diagonal1 = float(input('Ingrese la diagonal mayor del rombo: '))
		diagonal2 = float(input('Ingrese la diagonal menor del rombo: '))
		area = area_rombo(diagonal1, diagonal2)
		print('')
		print('El area del rombo es:', area)
		
	elif opcion == 4:
		
		radio = float(input('Ingrese el radio del circulo: '))
		area = area_circulo(radio)
		print('')
		print('El area del circulo es:', area)
		
	else:
		
		print('Opcion invalida. Por favor, seleccione una opcion valida.')