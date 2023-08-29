from math import pi

def area_rectangulo(l1,l2):
    return l1*l2
def area_circulo(r):
    return pi*r**2
def area_triangulo(base,h):
    return (base*h)/2
def area_rombo(D_mayor,D_menor):
    return (D_mayor*D_menor)/2

print(area_rectangulo(8,10))
print(area_circulo(6))
print(area_triangulo(10,15))
print(area_rombo(7,6))
