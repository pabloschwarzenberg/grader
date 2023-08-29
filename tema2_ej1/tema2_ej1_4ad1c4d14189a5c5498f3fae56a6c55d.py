import math
print('** ÁREAS GEOMÉTRICAS **')

def area_triangulo(base,altura):
    area = (base*altura)/2
    return area

def area_rectangulo(base,altura):
    area = (base*altura)
    return area

def area_rombo(diagonal1,diagonal2):
    area = (diagonal1*diagonal2)/2
    return area

def area_circulo(radio):
    area = (math.pi)*(radio**2)
    return area

if __name__ == "__main__":
    base_t = int(input('Ingrese base triangulo: '))
    altura_t = int(input('Ingrese altura triangulo: '))
    print(area_triangulo(base_t,altura_t))
    base_r = int(input('Ingrese base rectángulo: '))
    altura_r = int(input('Ingrese altura rectángulo: '))
    print(area_rectangulo(base_r,altura_r))
    diagonal1 = int(input('Ingrese primera diagonal del rombo: '))
    diagonal2 = int(input('Ingrese segunda diagonal del rombo: '))
    print(area_rombo(diagonal1,diagonal2))
    radio = int(input('Ingrese radio del círculo: '))
    print(area_circulo(radio))

           