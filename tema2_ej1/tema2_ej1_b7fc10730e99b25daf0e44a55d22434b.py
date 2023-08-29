def area_triangulo(base,altura):
    base=int(input("ingrese la base: "))
    altura=int(input("ingrese la altura: "))
    areat=base * altura / 2.0
    return areat
    pass
    
def area_rectangulo(base,altura):
    largo=int(input("ingrese el largo: "))
    ancho=int(input("ingrese el ancho: "))
    area=ancho*largo
    return area
    pass

def area_rombo(diagonal1,diagonal2):
    diagonal1=int(input("ingrese el largo de la diagonal mayor: "))
    diagonal2=int(input("ingrese le largo de la diagonal menor: "))
    arear= diagonal1*diagonal2 / 2
    return arear
    pass

def area_circulo(radio):
    radio=int(input("ingrese el radio: "))
    area=math.pi*radio**2
    return area
    pass

if __name__ == "__main__":
    pass
           