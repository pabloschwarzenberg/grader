from math import pi 

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
    area = pi * (radio ** 2)
    return area

if __name__ == "__main__":
    respuesta = input("¿Qué escoje calcular? triángulo, rectángulo, rombo, círculo")
    if respuesta == "triángulo":
        base = input("Ingrese la base: ")
        altura = input("Ingrese la altura: ")
        area_triangulo(base, altura)
    elif respuesta == "rectángulo":
        base = input("Ingrese la base: ")
        altura = input("Ingrese la altura: ")
        area_rectangulo(base, altura)
    elif respuesta == "rombo":
        diagonal1 = input("Ingrese la diagonal 1: ")
        diagonal2 = input("Ingrese la diagonal 2: ")
        area_rombo(diagonal1, diagonal2)
    elif respuesta == "círculo":
        radio = input("Ingrese el radio: ")
        area_circulo(radio)

    
           