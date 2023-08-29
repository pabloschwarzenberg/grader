import math
def area_triangulo(base,altura):
    area_triangulo = (base*altura)/2
    return area_triangulo
    pass

def area_rectangulo(base,altura):
    area_rectangulo = (base*altura)
    return area_rectangulo
    pass

def area_rombo(diagonal1,diagonal2):
    area_rombo = (diagonal1*diagonal2)/2
    return area_rombo
    pass

def area_circulo(radio):
    area_circulo = math.pi * radio ** 2
    return area_circulo
    pass

if __name__ == "__main__":
    base = float(input("Ingrese el valor de la base: "))
    altura = float(input("Ingrese el valor de la altura: "))
    diagonal1 = float(input("Ingrese el valor de diagonal 1 : "))
    diagonal2 = float(input("Ingrese el valor de diagonal 2 : "))
    radio = float(input("Ingrese el valor del radio: "))
    print("El area del triangulo es : ",area_triangulo(base,altura))
    print("El area del rectangulo es : ",area_rectangulo(base,altura))
    print("El area del rombo es : ",area_rombo(diagonal1,diagonal2))
    print("El area del circulo es :",area_circulo(radio))
    
    pass
           