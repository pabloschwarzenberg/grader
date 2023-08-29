from math import pi

def area_triangulo(base,altura):
    area=(base*altura)/2
    return area

def area_rectangulo(base,altura):
    area=base*altura
    return area

def area_rombo(diagonal1,diagonal2):
    area=(diagonal1*diagonal2)/2
    return area

def area_circulo(radio):
    area=pi*(radio**2)
    return area

if __name__ == "__main__":
    figura=input("cual es la figura triangulo(t) rectangulo(re) rombo(ro) circulo(c):")
    figura.lower()
    area=0
    if figura=="t":
        base=int(input("cual es la base: "))
        altura=int(input("cual es la altura: "))
        area=area_triangulo(base,altura)
    elif figura=="re":
        base=int(input("cual es la base: "))
        altura=int(input("cual es la altura: "))
        area=area_rectangulo(base,altura)
    elif figura=="ro":
        diagonal1=int(input("cual es la primera diagonal: "))
        diagonal2=int(input("cual es la segunda diagonal: "))
        area=area_rombo(diagonal1,diagonal2)
    elif figura=="c":
        radio=int(input("radio: "))
        area=area_circulo(radio)
    print(area)

           