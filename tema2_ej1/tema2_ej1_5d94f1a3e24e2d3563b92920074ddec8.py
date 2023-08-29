def area_triangulo(base,altura):
    tri=base*altura/2
    return tri
    pass

def area_rectangulo(base,altura):
    rec=base*altura
    return rec
    pass

def area_rombo(diagonal1,diagonal2):
    rom=diagonal1*diagonal2/2
    return rom
    pass

def area_circulo(radio):
    pi=3.141592653589793
    cir=radio*radio*pi
    return cir
    pass



if __name__ == "triangulo":
    base=float(input("base triángulo:"))
    altura=float(input("altura triángulo:"))
    print(area_triangulo())
    pass

if __name__== "rectangulo":
    base=float(input("base rectángulo:"))
    altura=float(input("altura rectángulo:"))
    print(area_rectangulo())
    pass

if __name__ == "rombo":
    diagonal1=float(input("diagonal 1:"))
    diagonal2=float(input("diagonal 2:"))
    print(area_rombo())
    pass

if __name__ == "circulo":
    radio=float(input("radio círculo:"))
    print(area_circulo())
    pass
           
           

           