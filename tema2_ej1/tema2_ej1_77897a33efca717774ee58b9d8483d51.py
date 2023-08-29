def area_triangulo(base,altura):
    areaTriangulo = (base*altura)/2
    return areaTriangulo
    pass

def area_rectangulo(base,altura):
    areaRectangulo = base*altura
    return areaRectangulo
    pass

def area_rombo(diagonal1,diagonal2):
    areaRombo = (diagonal1*diagonal2)/2
    return areaRombo
    pass

def area_circulo(radio):
    from math import pi
    areaCirculo = pi*radio**2
    return areaCirculo
    pass

if __name__ == "__main__":
    print(' MENÚ')
    print(' 1. Calcular Área Rectángulo')
    print(' 2. Calcular Área Triángulo')
    print(' 3. Calcular Área Rombo')
    print(' 4. Calcular Área Círculo')
    opcion = int(eval(input('Ingrese opción para calcular: ')))
    if opcion == 1:
        base = eval(input('Ingrese la base del rectángulo: '))
        altura = eval(input('Ingrese la altura del rectángulo: '))
        areaRect = area_rectangulo(base,altura)
        print(areaRect)
        
    if opcion == 2:
        base = eval(input('Ingrese la base del triángulo: '))
        altura = eval(input('Ingrese la altura del triángulo: '))
        areaTri = area_triangulo(base,altura)
        print(areaTri)
        
    if opcion == 3:
        diagonal1 = eval(input('Ingrese la diagonal 1 del rombo: '))
        diagonal2 = eval(input('Ingrese la diagonal 2 del rombo: '))
        areaRombo = area_rombo(diagonal1,diagonal2)
        print(areaRombo)
        
    if opcion == 4:
        radio = eval(input('Ingrese el radio del circulo: '))
        areaCirculo = area_circulo(radio)
        print(areaCirculo)
    pass
