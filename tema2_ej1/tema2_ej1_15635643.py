def area_triangulo(base,altura):
    area=base*altura/2
    return area
def area_rectangulo(base,altura):
    area=base*altura
    return area
def area_rombo(diagonal1,diagonal2):
    area=diagonal1*diagonal2/2
    return area
def area_circulo(radio):
    pi=3.141592653589793125
    area=pi*(radio**2)
    return area

if __name__ == "__main__":
    figura=str(input("Ingresa la figura para calcular su área: "))
    if figura=="triangulo":
        b=eval(input("Ingresa la base: "))
        h=eval(input("Ingresa la altura: "))
        print(area_triangulo(b,h))
    elif figura=="rectangulo":
        b=eval(input("Ingresa la base: "))
        h=eval(input("Ingresa la altura: "))
        print(area_rectangulo(b,h))
    else:
        if figura=="rombo":
            d1=eval(input("Ingresa la primera diagonal: "))
            d2=eval(input("Ingresa la segunda diagonal: "))
            print(area_rombo(d1,d2))
        elif figura=="circulo":
            r=eval(input("Ingresa el radio: "))
            print(area_circulo(r))