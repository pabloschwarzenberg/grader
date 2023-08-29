from math import pi
def area_triangulo(base,altura):
    area1 = (altura * base)/2
    print("El area del triangulo es:", area1)
    return area1
area_triangulo(4,9)
def area_rectangulo(base,altura):
    area2 = base * altura
    print("El area del rectangulo es:", area2)
    return area2
area_rectangulo(2,7)
def area_rombo(diagonal1,diagonal2):
    area3 = (diagonal1*diagonal2)/2
    print("El area del rombo es:" ,area3)
    return area3
area_rombo(1,8)
def area_circulo(radio):
    area4 = pi*(radio**2)
    print("EL area del circulo es: ",area4)
    return area4
area_circulo(2)
           