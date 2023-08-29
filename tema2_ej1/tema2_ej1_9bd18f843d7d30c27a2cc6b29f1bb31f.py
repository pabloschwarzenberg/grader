from math import pi
def area_triangulo(base,altura):
    at = (base*altura)/2
    return at
    pass

def area_rectangulo(base,altura):
    ar = base*altura
    return ar
    pass

def area_rombo(diagonal1,diagonal2):
    aro = (diagonal1*diagonal2)/2
    return aro
    pass

def area_circulo(radio):
    ac = pi*(radio**2)
    return ac
    pass
print('Area Triangulo: 1')
print('Area Rectangulo: 2')
print('Area Rombo: 3')
print('Area Circulo: 4')

if __name__ == "__main__":
    a = int(input('Area a calcular: '))
    if a == 1:
        b = int(input('base: '))
        h = int(input('altura: '))
        print(area_triangulo(b,h))
    elif a == 2:
        b = int(input('base: '))
        h = int(input('altura: '))
        print(area_rectangulo(b,h))
    elif a == 3:
        d1 = int(input('diagonal_1: '))
        d2 = int(input('diagonal_2: '))
        print(area_rombo(d1,d2))
    elif a == 4:
                r = float(input('radio: '))
                print(area_circulo(r))
    pass
           