from math import pi

def area_triangulo(base,altura):
    b = base
    a = altura
    areaT = ((b*a)/2)
    return areaT

def area_rectangulo(baser,alturar):
    brr = baser
    arr = alturar
    areaR = (brr*arr)
    return areaR

def area_rombo(diagonal1,diagonal2):
    d1 = diagonal1
    d2 = diagonal2
    areaRo = float((d1*d2)/2)
    return areaRo

def area_circulo(radio):
    r = radio
    areaC = (pi*r**2)
    return areaC