import math
def area_triangulo(base,altura):  
    area=base*altura/2
    return area
    pass

def area_rectangulo(base,altura):
    area=base*altura
    return area
    pass

def area_rombo(diagonal1,diagonal2):
    area=diagonal1*diagonal2
    return area
    pass

def area_circulo(radio):
    area=math.pi*radio**2
    return area
    pass

print("¿Que figura quiere calcular?")

if a==1:
    base=float(input("base: "))
    altura=float(input("altura: "))
    area_triangulo(base,altura)
    print(area_triangulo(base,altura))
elif a==2:
    base=float(input("base: "))
    altura=float(input("altura: "))
    area_rectangulo(base,altura)
    print(area_rectangulo(base,altura))
elif a==3:
    diagonal1=float(input("diagonal 1:"))
    diagonal2=float(input("diagonal 2:"))
    area_rombo(diagonal1,diagonal2)
    print(area_rombo(diagonal1,diagonal2))
elif a==4:
    radio=float(input("radio: "))
    area_circulo(radio)
    print(area_circulo(radio))


if __name__ == "__main__":
    a=int(input("a: "))
    pass