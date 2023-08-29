def area_triangulo(base,altura):
    Area = (base*altura)/2
    return Area
    pass

def area_rectangulo(base,altura):
    Area = base*altura
    return Area
    pass

def area_rombo(diagonal1,diagonal2):
    Area = (diagonal1*diagonal2)/2
    return Area
    pass

def area_circulo(radio):
    import math
    Area = math.pi*(radio**2)
    return Area
    pass
rombo =  0
circulo = 1
triangulo = 2
rectangulo = 3
print("Este programa calcula el area de 4 figuras geometricas")
print("seleccione entre circulo,rombo,rectangulo y triangulo")

if __name__ == "__main__":
    n = eval(input("ingrese la figura que desea calcular el area"))
    if n == rombo:
        c = int(input("ingrese diagonal 1"))
        d = int(input("ingrese diagonal 2"))
        print("El Area del rombo es de ", area_rombo(c,d),"cm cuadrados")
    elif n == circulo:
        e = int(input("ingrese radio"))
        print("El Area del circulo es de ", area_circulo(e),"cm cuadrados")
    elif n == rectangulo:
        f = int(input("ingrese base"))
        g = int(input("ingrese altura"))
        print("El Area del rectangulo es de ", area_rectangulo(f,g),"cm cuadrados")
    elif n == triangulo:
        h = int(input("ingrese base"))
        j = int(input("ingrese altura"))
        print("El Area del triangulo es de ", area_triangulo(h,j),"cm cuadrados")

    pass
