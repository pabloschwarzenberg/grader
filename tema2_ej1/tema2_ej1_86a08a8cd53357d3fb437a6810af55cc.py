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
    import math
    area = (math.pi * radio**2)
    return area

if __name__ == "__main__":
    print("1=Triángulo")
    print("2=Rectángulo")
    print("3=Rombo")
    print("4=Círculo")
    opcion = int(input("¿Qué área deseas calcular?:"))
    if opcion == 1:
        base = int(input("Base del triángulo:"))
        altura = int(input("Altura del triángulo:"))
        print("El área es", area_triangulo(base,altura))
    elif opcion == 2:
        base = int(input("Base del rectángulo:"))
        altura = int(input("Altura del rectángulo:"))
        print("El área es", area_rectangulo(base,altura))
    elif opcion == 3:
        diagonal1 = int(input("Diagonal del rombo:"))
        diagonal2 = int(input("Otra diagonal del rombo:"))
        print("El área es", area_rombo(diagonal1,diagonal2))
    elif opcion == 4:
        radio = int(input("Radio de la circunferencia:"))
        print("El área es", area_circulo(radio))
           