import math
print('Que desea calcular: \n1) area triangulo\n2) area rectangulo\n3) area rombo\n4) area circulo')
q = 'area_triangulo'
 
def area_triangulo(base,altura):
    area_triangulo = (base * altura)/2
    return area_triangulo

def area_rectangulo(base,altura):
    area_rectangulo = (base*altura)
    return area_rectangulo

def area_rombo(diagonal1,diagonal2):
    area_rombo = (diagonal1*diagonal2)/2
    return area_rombo

def area_circulo(radio):
    area_circulo = (math.pi)  * (radio**2)
    return area_circulo

if  q == 'area_triangulo':
    base = 12
    altura = 6
    print(area_triangulo(base,altura))

elif q == 'area_rectangulo':
    base = 12
    altura = 6
    print(area_rectangulo(base,altura))

elif q == 'area_rombo':
    d1 = 12
    d2 = 12
    print(area_rombo(d1,d2))

elif q == 'area_circulo':
    r = 8
    print(area_circulo(r))

