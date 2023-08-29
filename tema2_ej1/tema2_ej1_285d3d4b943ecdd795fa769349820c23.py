from math import pi
def area_triangulo(base,altura):
    area = (base*altura)/2
    return area

def area_rectangulo(base,altura):
    area = base*altura
    return area

def area_rombo(diagonal1,diagonal2):
    area = (diagonal1*diagonal2)/2
    return area

def area_circulo(radio):
    area = (radio*radio)*pi
    return area


if __name__=="__main__": 

    print("ingrese el numero de la figura")
    figura=int(input("1.triangulo, 2.rectangulo, 3.rombo, 4.circulo:"))

    if figura == 1:
        base = int(input("ingrese el valor de la base:"))
        altura = int(input("ingrese el valor de la latura:"))
        
        area_triangulo(base,altura)
        
    if figura == 2:
        base = int(input("ingrese el valor de la base:"))
        altura = int(input("ingrese el valor de la latura:"))
      
        area_rectangulo(base,altura)
        
    if figura == 3:
        base = int(input("ingrese el valor de la diagonal1:"))
        altura = int(input("ingrese el valor de la diagonal2:"))

        area_rombo(diagonal1,diagonal2)
    if figura == 4:
        radio = int(input("ingrese el valor del radio:"))

        area_circulo(radio)