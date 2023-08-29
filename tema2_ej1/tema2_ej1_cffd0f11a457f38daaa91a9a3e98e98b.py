def area_triangulo(base,altura):
    AreaTriangulo = (base * altura)/2
    return AreaTriangulo

def area_rectangulo(base,altura):
    AreaRectangulo = base * altura
    return AreaRectangulo

def area_rombo(diagonal1,diagonal2):
    AreaRombo = (diagonal1 * diagonal2)/2
    return AreaRombo

def area_circulo(radio):
    pi = 3.1415926535897932
    AreaCirculo = pi * radio**2
    return AreaCirculo
def numero_perfecto(a):
    suma = 0
    for i in range(1,a):
       if (a % (i) == 0):
          suma += (i)
    if a == suma:
       return True
    else:
       return False