import math
def area_triangulo(base,altura):
	area = (base * altura)/2
	return area
	

def area_rectangulo(base,altura):
	area = base * altura
	return area
	

def area_rombo(diagonal1,diagonal2):
	area = (diagonal1 * diagonal2)/2
	return area

def area_circulo(radio):
	area = math.pi*radio**2
	return area

if __name__ == "__main__":
	print('Area triangulo (1)\nArea rectangulo (2)\nArea rombo(3)\nArea circulo(4)')
	escoger = int(input(''))
	if escoger == 1:
		base = int(input('Ingrese una base: '))
		altura = int(input('Ingrese una altura: '))
		area_triangulo(base,altura)
	if escoger == 2:
		base = int(input('Ingrese una base: '))
		altura = int(input('Ingrese una altura: '))
		area_rectangulo(base,altura)
	if escoger == 3:
		diagonal1 = int(input('Ingrese una diagonal1: '))
		diagonal2 = int(input('Ingrese una diagonal2: '))
		area_rombo(diagonal1,diagonal2)
	if escoger == 4:
		radio = int(input('Ingrese un radio: '))
		area_circulo(radio)

           