from math import pi

def area_triangulo(base,altura):
    AreaDelTriangulo = (base*altura)/2
    return AreaDelTriangulo
    pass


def area_rectangulo(base,altura):
    AreaDelRectangulo = (base*altura)
    return AreaDelRectangulo
    pass
  

def area_rombo(diagonal1,diagonal2):
    AreaDelRombo = (diagonal1*diagonal2)/2
    return AreaDelRombo
    pass

def area_circulo(radio):
    AreaDelCirculo = pi*radio**2
    return AreaDelCirculo
    pass

if __name__ == "__main__":
    b = int(input("Ingrese la base del triangulo: "))
    a = int(input("Ingrese la altura del triangulo: "))
    print(area_triangulo(b,a))
    b = int(input("Ingrese la base del rectangulo: "))
    a = int(input("Ingrese la altura del rectangulo: "))
    print(area_rectangulo(b,a))
    diagonal1 = int(input("Ingrese la base del rombo: "))
    diagonal2 = int(input("Ingresa la altura del rombo: "))
    print(area_rombo(diagonal1,diagonal2))
    radio = int(input("Ingrese el radio del circulo: "))
    print(area_circulo(radio))
    pass
           