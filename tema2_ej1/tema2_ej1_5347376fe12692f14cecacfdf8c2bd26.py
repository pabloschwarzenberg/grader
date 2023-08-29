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
    import math
    area = math.pi * (radio ** 2)
    return area

if __name__ == "__main__":
    print('Opcion 1: Area de un triangulo')
    print('Opcion 2: Area de un rectangulo')
    print('Opcion 3: Area de un rombo')
    print('Opcion 4: Area de un circulo')
    opcion = int(input('Elige la una opcion: '))
    if opcion == 1:
        b = float(input('Indique base del triangulo: '))
        a = float(input('Indique altura del triangulo: '))
        print(area_triangulo(b,a))
    elif opcion == 2:
        b = float(input('Indique base del rectangulo: '))
        a = float(input('Indique altura del rectangulo: '))
        print(area_rectangulo(b,a))
    elif opcion == 3:
        b = float(input('Indique la diagonal 1 del rombo: '))
        a = float(input('Indique la diagonal 2 del rombo: '))
        print(area_rombo(b,a))
    elif opcion == 4:
        a = float(input('Indique el radio del circulo: '))
        print(area_circulo(a))
    pass
           