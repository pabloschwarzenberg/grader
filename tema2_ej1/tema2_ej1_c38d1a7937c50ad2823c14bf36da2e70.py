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
	area = math.pi * (radio**2)
	return area

if __name__ == "__main__":
    print("1. Calcular area de un triangulo")
    print("2. Calcular area de un rectangulo")
    print("3. Calcular area de un rombo")
    print("4. Calcular area de un circulo")
    op = int(input("Ingrese lo que desea calcular: "))
    if op == 1:
    	base = int(input("Ingrese la medida de la base del triangulo: "))
    	altura = int(input("Ingrese la medida de la altura del triangulo: "))
    	print("El resultado es: ", area_triangulo(base, altura))
    elif op == 2:
    	base = int(input("Ingrese la medida de la base del rectangulo: "))
    	altura = int(input("Ingrese la medida de la altura del rectangulo: "))
    	print("El resultado es: ", area_rectangulo(base, altura))
    elif op == 3:
    	d1 = int(input("Ingrese la medida de la primera diagonal del rombo: "))
    	d2 = int(input("Ingrese la medida de la segunda diagonal del rombo: "))
    	print("El resultado es: ", area_rombo(d1, d2))
    elif op == 4:
    	radio = float(input("Ingrese la medida del radio del circulo: "))
    	print("El resultado es: ", area_circulo(radio))
    else:
    	print("Ingrese opcion correcta")
           