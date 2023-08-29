def area_triangulo(base,altura):
    area_triangulo = (base * altura)/2
    global area
    area = area_triangulo
    return area_triangulo

def area_rectangulo(base,altura):
    area_rectangulo = base * altura
    global area
    area = area_rectangulo
    return area_rectangulo

def area_rombo(diagonal1,diagonal2):
    area_rombo = (diagonal1 * diagonal2)/2
    global area
    area = area_rombo
    return area_rombo

def area_circulo(radio):
    import math
    area_circulo = math.pi * (radio) ** 2
    print(area_circulo)
    global area
    area = area_circulo
    return area_circulo

if __name__ == "__main__":
    base = int(input("Ingrese la base del triangulo"))
    altura = int(input("Ingrese la altura del triangulo"))
    if(area_triangulo(base,altura) == area):
        print(area)
        base = int(input("Ingrese la base del rectangulo"))
        altura = int(input("Ingrese la altura del rectangulo"))
        if(area_rectangulo(base,altura) == area):
            print(area)
            diagonal1 = int(input("Ingrese la primera diagonal del rombo"))
            diagonal2 = int(input("Ingrese la segundo diagonal del rombo"))
            if(area_rombo(diagonal1,diagonal2) == area):
                print(area)
                radio = int(input("Ingrese el radio del circulo"))
                if(area_circulo(radio) == area):
                    print(area)
    
           