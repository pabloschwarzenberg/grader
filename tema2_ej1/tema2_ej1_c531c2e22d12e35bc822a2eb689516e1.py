from math import pi

def area_triangulo(base,altura):
    areaT = ((base*altura)/2)
    #print("El área del triangulo es: ", float(areaT))
    return areaT

def area_rectangulo(base,altura):
    areaR = base*altura
    #print("El área del rectángulo es: ", int(areaR))
    return areaR

def area_rombo(diagonal1,diagonal2):
    areaRO = ((diagonal1*diagonal2)/2)
    #print("El área del rombo es: ", float(areaRO))
    return areaRO

def area_circulo(radio):
    areaC = ((pi)*(radio**2))
    #print("El área del circulo es: ", float(areaC))
    return areaC

#if __name__ == "__main__":
#    pass
           