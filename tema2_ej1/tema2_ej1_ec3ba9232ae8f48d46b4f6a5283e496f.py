import math
def area_triangulo(base,altura):
    x=base
    y=altura
    area=(base*altura)/2
    return area
def area_rectangulo(base,altura):
    x=base
    y=altura
    area=base*altura
    return area
def area_rombo(diagonal1,diagonal2):
    x=diagonal1
    y=diagonal2
    area=(x*y)/2
    return area
def area_circulo(radio):
    x=radio
    area=math.pi*radio**2
    return area
if __name__ == "__main__": 
    x=eval((input("elija la figura que desea calcular el area:")))
    print("1.triangulo")
    print("2.rectangulo")
    print("3.rombo")
    print("4.circulo")
    if x==1:
       print(area_triangulo(eval(input("Ingrese base:")),eval(input("Ingrese altura:"))))
    elif x==2:
       print(area_rectangulo(eval(input("Ingrese base:")),eval(input("Ingrese altura:"))))
    elif x==3:
       print(area_rombo(eval(input("Ingrese diagonal 1:")),eval(input("Ingrese diagonal 2:"))))
    elif x==4:
       print(area_circulo(eval(input("Ingrese radio:"))))

           