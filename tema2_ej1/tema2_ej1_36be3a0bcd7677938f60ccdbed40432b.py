def area_triangulo(base,altura):
    base = float(base)
    altura = float(altura)
    area = (base*altura)/2
    return area
    pass

def area_rectangulo(base,altura):
    base = float(base)
    altura = float(altura)
    area = base*altura
    return area
    
    pass

def area_rombo(diagonal1,diagonal2):
    diagonal1 = float(diagonal1)
    diagonal2 = float(diagonal2)
    areaA = (diagonal1*diagonal2)
    areaB = areaA/2
    return areaB
    pass

def area_circulo(radio):
    radio = float(radio)
    pi = 3.141592653589793
    area = pi*(radio**2)
    return area
    pass
if __name__ == "__main__":
    pass
           