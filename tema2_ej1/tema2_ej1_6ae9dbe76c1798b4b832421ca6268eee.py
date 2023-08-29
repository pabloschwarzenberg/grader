def area_triangulo(base,altura):
    return (base * altura)/2
    pass

def area_rectangulo(base,altura):
    return base * altura
    pass

def area_rombo(diagonal1,diagonal2):
    return (diagonal1 * diagonal2)/2
    pass

def area_circulo(radio):
    from math import pi
    return pi*radio*radio
    pass

if __name__ == "__main__":
    print (area_triangulo (11,7))
    print (area_rectangulo(10,6))
    print (area_rombo(30,16))
    print (area_circulo(40))
    pass