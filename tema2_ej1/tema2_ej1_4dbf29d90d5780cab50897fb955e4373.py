import math
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
    area=math.pi*radio*radio
    return area

rombo="rombo"
triangulo="triangulo"
circulo="circulo"
rectangulo="rectangulo"

figura=input("a que figura le deseas calcular su area?: ")

if  figura==rectangulo:
    lado1=int(input("lado: "))
    lado2=int(input("base: "))
    area=area_rectangulo(lado1,lado2)
    print("el ",figura,"tiene area ", area)

if figura==triangulo:
    lado1=int(input("base: "))
    lado2=int(input("altura: "))
    area=int(area_triangulo(lado1,lado2))
    print("el ",figura,"tiene area ", area)
if figura==rombo:
    diagonal1=int(input("diagonal 1: "))
    diagonal2=int(input("diagonal 2:"))
    area=int(area_rombo(diagonal1,diagonal2))
    print("el ",figura," tiene area ",area)

if figura==circulo:
    radio=int(input("radio: "))
    area=int(area_circulo(radio))
    print("el ",figura," tiene area ",area)