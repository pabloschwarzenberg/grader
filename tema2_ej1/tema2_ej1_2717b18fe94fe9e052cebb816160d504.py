#Calculadora geométrica

import math

def area_triangulo(base,altura):
	area = (base * altura) / 2

	return area

def area_rectangulo(base,altura):
    area = base * altura

    return area

def area_rombo(diagonal1,diagonal2):
    area = (diagonal1 * diagonal2) / 2

    return area

def area_circulo(radio):
    area = math.pi * radio**2

    return area

def main():
	print("Calculadora geométrica")
	print("1: Triangulo, 2: Rectangulo, 3: Rombo, 4: Círculo")
	menu = int(input("Seleccione operación: "))
	if(menu == 1):
		x = float(input("Ingrese base: "))
		y = float(input("Ingrese altura: "))
		print(area_triangulo(x, y))
	elif(menu == 2):
		x = float(input("Ingrese base: "))
		y = float(input("Ingrese altura: "))
		print(area_rectangulo(x, y))
	elif(menu == 3):
		x = float(input("Ingrese diagonal1: "))
		y = float(input("Ingrese diagonal2: "))
		print(area_rombo(x, y))
	elif(menu == 4):
		x = float(input("Ingrese radio: "))
		print(area_circulo(x))

if __name__ == "__main__":
    main()
           