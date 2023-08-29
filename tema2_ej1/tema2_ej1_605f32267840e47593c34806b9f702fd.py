from math import pi

def area_triangulo(base,altura):
    area = (base*altura)/2
    return area

def area_rectangulo(base,altura):
    area = base * altura
    return area

def area_rombo(diagonal1,diagonal2):
    area = (diagonal1 * diagonal2)/2
    return area

def area_circulo(radio):
    area = pi * (radio**2)
    return area

triangulo = area_triangulo
rectangulo = area_rectangulo
rombo = area_rombo
circulo = area_circulo

if __name__ == "__main__":
    print("-Calculadora de area-")
    area_deseada = input("¿Desea sacar el area de un triangulo, rectangulo, rombo o circulo?: ")
    
    if area_deseada == "triangulo":
        base = int(input("Ingrese la base de su Triangulo: "))
        altura = int(input("Ingrese la altura de su Triangulo: "))
        print("Su area es:", area_triangulo(base,altura))

    elif area_deseada == "rectangulo":
        base = int(input("Ingrese la base de su Rectangulo: "))
        altura = int(input("Ingrese la altura de su Rectangulo: "))
        print("Su area es:", area_rectangulo(base, altura))
        
    elif area_deseada == "rombo":
        diagonal1 = int(input("Ingrese la diagonal mayor de su Rombo: "))
        diagonal2 = int(input("Ingrese la diagonal menor de su Rombo: "))
        print("Su area es:", area_rombo(diagonal1, diagonal2))
        
    elif area_deseada == "circulo":
        radio = int(input("Ingrese el radio de su Circulo: "))
        print("Su area es:", area_circulo(radio))
    else:
        print("Opción no valida")